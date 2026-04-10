#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from html import unescape
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCK_DIR = ROOT / "tests" / "non-regression" / "locks"


TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")


def normalize(text: str) -> str:
    text = unescape(text)
    text = TAG_RE.sub(" ", text)
    return SPACE_RE.sub(" ", text).strip()


def extract_heading_and_core_texts(html: str) -> list[str]:
    candidates: list[str] = []

    patterns = [
        r"<h1[^>]*>(.*?)</h1>",
        r"<h2[^>]*>(.*?)</h2>",
        r"<h3[^>]*>(.*?)</h3>",
        r"<p[^>]*class=[\"'][^\"']*hero-copy[^\"']*[\"'][^>]*>(.*?)</p>",
    ]

    for pattern in patterns:
        for raw in re.findall(pattern, html, flags=re.IGNORECASE | re.DOTALL):
            text = normalize(raw)
            if text:
                candidates.append(text)

    unique: list[str] = []
    seen: set[str] = set()
    for c in candidates:
        key = c.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(c)

    return unique


def extract_images(html: str) -> list[str]:
    srcs = re.findall(r"<img[^>]+src=[\"']([^\"']+)[\"']", html, flags=re.IGNORECASE)
    unique: list[str] = []
    seen: set[str] = set()
    for src in srcs:
        s = src.strip()
        if not s:
            continue
        if s in seen:
            continue
        seen.add(s)
        unique.append(s)
    return unique


def lock_id_from_target(target: Path) -> str:
    stem = target.stem.lower().replace("_", "-")
    return stem


def cmd_lock(args: argparse.Namespace) -> int:
    target = (ROOT / args.target).resolve() if not Path(args.target).is_absolute() else Path(args.target)
    if not target.exists():
        print(f"[error] Target file not found: {target}")
        return 1

    html = target.read_text(encoding="utf-8")
    texts = extract_heading_and_core_texts(html)
    images = extract_images(html)

    if args.max_texts > 0:
        texts = texts[: args.max_texts]

    lock_id = args.id or lock_id_from_target(target)
    lock_dir = Path(args.lock_dir)
    if not lock_dir.is_absolute():
        lock_dir = (ROOT / lock_dir).resolve()
    lock_dir.mkdir(parents=True, exist_ok=True)

    rel_target = str(target.resolve().relative_to(ROOT))
    lock_path = lock_dir / f"{lock_id}.lock.json"

    payload = {
        "id": lock_id,
        "file": rel_target,
        "required_texts": texts,
        "required_images": images,
    }
    lock_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"[ok] Lock written: {lock_path}")
    print(f"     required_texts: {len(texts)}")
    print(f"     required_images: {len(images)}")
    return 0


def load_lock_files(lock_dir: Path, only_id: str | None) -> list[Path]:
    if only_id:
        p = lock_dir / f"{only_id}.lock.json"
        return [p] if p.exists() else []
    return sorted(lock_dir.glob("*.lock.json"))


def missing_items(required: Iterable[str], haystack: str) -> list[str]:
    norm_hay = normalize(haystack).lower()
    missing: list[str] = []
    for item in required:
        if normalize(item).lower() not in norm_hay:
            missing.append(item)
    return missing


def cmd_check(args: argparse.Namespace) -> int:
    lock_dir = Path(args.lock_dir)
    if not lock_dir.is_absolute():
        lock_dir = (ROOT / lock_dir).resolve()

    lock_files = load_lock_files(lock_dir, args.id)
    if not lock_files:
        print(f"[warn] No lock files found in {lock_dir}")
        return 0

    failures = 0
    for lock_file in lock_files:
        data = json.loads(lock_file.read_text(encoding="utf-8"))
        rel = data.get("file", "")
        target = (ROOT / rel).resolve()

        print(f"\n[check] {data.get('id', lock_file.stem)} -> {rel}")
        if not target.exists():
            print(f"  [fail] Target file missing: {target}")
            failures += 1
            continue

        html = target.read_text(encoding="utf-8")
        miss_texts = missing_items(data.get("required_texts", []), html)
        current_imgs = set(extract_images(html))
        req_imgs = data.get("required_images", [])
        miss_imgs = [img for img in req_imgs if img not in current_imgs]

        if miss_texts or miss_imgs:
            failures += 1
            if miss_texts:
                print(f"  [fail] Missing required texts ({len(miss_texts)}):")
                for t in miss_texts:
                    print(f"    - {t}")
            if miss_imgs:
                print(f"  [fail] Missing required images ({len(miss_imgs)}):")
                for src in miss_imgs:
                    print(f"    - {src}")
        else:
            print("  [ok] No regressions detected for locked texts/images")

    if failures:
        print(f"\n[result] FAIL - {failures} lock file(s) with regressions")
        return 1

    print("\n[result] PASS - all locked modules are stable")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lock/check non-regression for finalized module texts and images"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_lock = sub.add_parser("lock", help="Create/update a lock file for a module page")
    p_lock.add_argument("target", help="Target HTML file, e.g. site/chapters/chapter-01.html")
    p_lock.add_argument("--id", help="Lock id, e.g. M1")
    p_lock.add_argument("--max-texts", type=int, default=24, help="Max required texts to persist")
    p_lock.add_argument(
        "--lock-dir",
        default=str(DEFAULT_LOCK_DIR.relative_to(ROOT)),
        help="Directory where lock files are stored",
    )
    p_lock.set_defaults(func=cmd_lock)

    p_check = sub.add_parser("check", help="Check all lock files for regressions")
    p_check.add_argument("--id", help="Check a single lock id")
    p_check.add_argument(
        "--lock-dir",
        default=str(DEFAULT_LOCK_DIR.relative_to(ROOT)),
        help="Directory where lock files are stored",
    )
    p_check.set_defaults(func=cmd_check)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
