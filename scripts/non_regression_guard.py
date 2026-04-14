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
MODULE_FILE_RE = re.compile(r"^site/chapters/chapter-\d+\.html$")

REQUIRED_UI_MARKERS: list[tuple[str, re.Pattern[str]]] = [
    # Fixed UI is now injected via site.js, so we don't check it in static HTML files
    ("Left outline nav", re.compile(r'id="outline-nav"', re.IGNORECASE)),
]


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


def extract_heading_tags(html: str, tag: str) -> list[str]:
    return re.findall(fr"<{tag}\b[^>]*>.*?</{tag}>", html, flags=re.IGNORECASE | re.DOTALL)


def check_required_ui_markers(html: str) -> list[str]:
    missing: list[str] = []
    for label, pattern in REQUIRED_UI_MARKERS:
        if not pattern.search(html):
            missing.append(label)
    return missing


def check_two_level_structure(html: str) -> list[str]:
    issues: list[str] = []
    h2s = extract_heading_tags(html, "h2")
    h3s = extract_heading_tags(html, "h3")
    deep = re.search(r"<h[4-6]\b", html, flags=re.IGNORECASE)

    if len(h2s) == 0:
        issues.append("Missing level-1 module headings (h2)")
    if len(h3s) == 0:
        issues.append("Missing level-1.1 subsection headings (h3)")
    if deep:
        issues.append("Found heading levels deeper than h3 (h4/h5/h6)")

    # Ensure every h3 appears after at least one h2 in document order.
    first_h2 = re.search(r"<h2\b", html, flags=re.IGNORECASE)
    if h3s and not first_h2:
        issues.append("Found h3 headings but no h2 heading")
    elif h3s and first_h2:
        first_h2_pos = first_h2.start()
        first_h3 = re.search(r"<h3\b", html, flags=re.IGNORECASE)
        if first_h3 and first_h3.start() < first_h2_pos:
            issues.append("Found h3 before first h2")

    return issues


def check_heading_numbering(html: str) -> list[str]:
    issues: list[str] = []
    heading_matches = re.finditer(
        r"<(h2|h3)\b[^>]*>(.*?)</\1>", html, flags=re.IGNORECASE | re.DOTALL
    )

    numbered: list[tuple[str, tuple[int, ...], str]] = []
    num_re = re.compile(r"^\s*(\d+(?:\.\d+)*)(?:\.)?\s+")

    for m in heading_matches:
        tag = m.group(1).lower()
        text = normalize(m.group(2))
        n = num_re.match(text)
        if not n:
            continue
        parts = tuple(int(p) for p in n.group(1).split("."))
        numbered.append((tag, parts, text))

    # Duplicates (same heading level + same numeric identifier)
    seen_ids: set[tuple[str, tuple[int, ...]]] = set()
    for tag, parts, text in numbered:
        key = (tag, parts)
        if key in seen_ids:
            pretty = ".".join(str(p) for p in parts)
            issues.append(f"Duplicate numbering in {tag}: {pretty} ({text})")
            continue
        seen_ids.add(key)

    # Sequential siblings: for same heading tag + same prefix, last component must increase by 1.
    last_seen: dict[tuple[str, tuple[int, ...]], int] = {}
    for tag, parts, text in numbered:
        if len(parts) == 0:
            continue
        prefix = parts[:-1]
        key = (tag, prefix)
        current = parts[-1]
        if key in last_seen:
            expected = last_seen[key] + 1
            if current != expected:
                pfx = ".".join(str(p) for p in prefix)
                family = f"{tag} {pfx}" if pfx else tag
                issues.append(
                    f"Non-sequential numbering in {family}: expected *.{expected}, found *.{current} ({text})"
                )
        last_seen[key] = current

    # Every numbered h3 should map to an existing numbered h2 parent.
    h2_numbers = {parts for tag, parts, _ in numbered if tag == "h2"}
    for tag, parts, text in numbered:
        if tag != "h3":
            continue
        if len(parts) < 2:
            issues.append(f"h3 heading should use hierarchical numbering (e.g., 1.1): {text}")
            continue
        parent = parts[:-1]
        if parent not in h2_numbers:
            parent_txt = ".".join(str(p) for p in parent)
            issues.append(f"h3 heading parent not found in h2 numbering: {text} (missing {parent_txt})")

    return issues


def check_module_flow(html: str) -> list[str]:
    issues: list[str] = []
    headings = [normalize(h) for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", html, flags=re.IGNORECASE | re.DOTALL)]
    
    if not any("Topics" in h for h in headings):
        issues.append("Missing 'Topics' section")
    if not any("Learning outcomes" in h for h in headings):
        issues.append("Missing 'Learning outcomes' section")
    
    # Check initial position (info-grid)
    article_start = html.find("<article")
    info_grid_pos = html.find('class="panel info-grid"')
    if info_grid_pos == -1:
        issues.append("Missing 'info-grid' panel for Topics and Learning outcomes")
    elif info_grid_pos < article_start:
        issues.append("'info-grid' must be inside the article")

    # Check terminal sections
    if not any("Guided lab" in h for h in headings):
        issues.append("Missing 'Guided lab' section")
    if not any("Key takeaways" in h for h in headings):
        issues.append("Missing 'Key takeaways' section")
        
    guided_pos = html.find("Guided lab")
    takeaways_pos = html.find("Key takeaways")
    if guided_pos != -1 and takeaways_pos != -1:
        if guided_pos > takeaways_pos:
            issues.append("'Key takeaways' should follow 'Guided lab'")

    return issues


def check_ui_logic(root_path: Path) -> list[str]:
    issues: list[str] = []
    js_file = root_path / "site" / "assets" / "js" / "site.js"
    css_file = root_path / "site" / "assets" / "css" / "site.css"
    
    if js_file.exists():
        js_content = js_file.read_text()
        if "outline-toggle-spacer" not in js_content:
            issues.append("JS: Missing logic for 'outline-toggle-spacer' in navigation menu")
        if "toggle.addEventListener" not in js_content:
            issues.append("JS: Missing event listener for navigation toggle")
            
    if css_file.exists():
        css_content = css_file.read_text()
        if ".outline-toggle-spacer" not in css_content:
            issues.append("CSS: Missing style for '.outline-toggle-spacer'")
        if "position: fixed" not in css_content or ".print-fixed" not in css_content:
            issues.append("CSS: Missing style for fixed 'Print' button")
            
    return issues


def cmd_check(args: argparse.Namespace) -> int:
    lock_dir = Path(args.lock_dir)
    if not lock_dir.is_absolute():
        lock_dir = (ROOT / lock_dir).resolve()

    failures = 0
    lock_files = load_lock_files(lock_dir, args.id)
    if not lock_files:
        print(f"[warn] No lock files found in {lock_dir}")
    else:
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

    # Global UI Logic Check
    print("\n[logic] Checking JS/CSS non-regression...")
    ui_logic_issues = check_ui_logic(ROOT)
    if ui_logic_issues:
        failures += 1
        for issue in ui_logic_issues:
            print(f"  [fail] {issue}")
    else:
        print("  [ok] UI logic for navigation and fixed buttons is present")

    module_files = sorted((ROOT / "site" / "chapters").glob("chapter-*.html"))
    if not module_files:
        print("\n[warn] No module pages found under site/chapters")
    else:
        for module_file in module_files:
            rel = str(module_file.resolve().relative_to(ROOT))
            if not MODULE_FILE_RE.match(rel):
                continue

            html = module_file.read_text(encoding="utf-8")
            miss_ui = check_required_ui_markers(html)
            structure_issues = check_two_level_structure(html)
            numbering_issues = check_heading_numbering(html)
            flow_issues = check_module_flow(html)

            print(f"\n[structure] {rel}")
            if miss_ui or structure_issues or numbering_issues or flow_issues:
                failures += 1
                if miss_ui:
                    print(f"  [fail] Missing required UI controls ({len(miss_ui)}):")
                    for item in miss_ui:
                        print(f"    - {item}")
                if structure_issues:
                    print(f"  [fail] Heading structure issues ({len(structure_issues)}):")
                    for issue in structure_issues:
                        print(f"    - {issue}")
                if numbering_issues:
                    print(f"  [fail] Heading numbering issues ({len(numbering_issues)}):")
                    for issue in numbering_issues:
                        print(f"    - {issue}")
                if flow_issues:
                    print(f"  [fail] Module flow issues ({len(flow_issues)}):")
                    for issue in flow_issues:
                        print(f"    - {issue}")
            else:
                print("  [ok] UI controls, structure, numbering, and flow are valid")

    if failures:
        print(f"\n[result] FAIL - {failures} check(s) with regressions")
        return 1

    print("\n[result] PASS - all modules and logic are compliant")
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
