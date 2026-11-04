# AGENTS.md

## Project Purpose

This repository contains the full production workspace for the **AI Agent Programming Course** website and materials.

Primary goals:
- build and maintain the interactive static course site
- produce module-by-module teaching materials, labs, and exercises
- preserve approved content stability through non-regression checks

Main language policy:
- source content is authored in English
- Italian is provided on-page via Google Translate switch (`EN/IT`)

Runtime baseline for examples:
- use local `ollama` runtime on Ubuntu
- default model: `gemma4:e4b`
- avoid dependence on OpenAI API keys for classroom examples

## Companion Repository (Code)

All runnable course code lives in the companion repo **`building-llm-applications`**:
- local path: `/home/thimoty/git/building-llm-applications` (GitHub: `thimotyb/building-llm-applications`)
- code for labs, exercises, demos and workshops goes there (chapters `ch01`...`ch13`, ADK in `ch12`, A2A/Docker in `ch13`); this repo holds only the site, notes, and course materials
- API keys and provider selection live in its git-ignored `.env` (`LLM_PROVIDER`, `OLLAMA_MODEL`, `GEMINI_API_KEY`, `DEEPSEEK_API_KEY`, `TYPESAFE_API_KEY`, ...); never copy keys into this repo
- the Workshop 2 plan is in `notes/TODO-seminar.md`

## Canonical Project Structure

Use this structure as the baseline:

- `site/index.html`: course homepage
- `site/chapters/chapter-XX.html`: one file per module
- `site/assets/css/site.css`: shared visual system and layout
- `site/assets/js/site.js`: shared behavior (language switch, outline nav, print, interactions)
- `site/assets/images/`: module images and figures
- `site/assets/downloads/`: downloadable assets
- `course-structure.md`: canonical module/source mapping
- `resources/`: raw source material and references
- `tests/non-regression/locks/`: lock files for finalized modules
- `scripts/non_regression_guard.py`: lock/check utility for non-regression

## Finalized Module Set

The course module structure is finalized as:

- `M1`: Getting Started with LLMs and LangChain
- `M2`: Summarization with LangChain and LangGraph
- `M3`: RAG Systems
- `M4`: Advanced RAG
- `M5`: AI Agents Architectures with LangGraph
- `M6`: Google Agent Development Kit
- `M7`: Labs and Exercises from Building LLM Applications

Each module must have:
- one dedicated chapter page (`chapter-01.html` ... `chapter-07.html`)
- coherent previous/current/next navigation
- aligned metadata in `course-structure.md`

## Module Content Structure (Required)

Each module page must use a two-level hierarchy:

- `Titolo 1` (section level) -> HTML `h2`
- `Titolo 1.1` (subsection level) -> HTML `h3`

Rules:
- sections and subsections must be explicitly numbered
- course numbering is authoritative and may differ from source/book numbering
- each subsection (`h3`) is rendered as one dedicated slide-like rectangular block
- avoid flat, unstructured content blocks
- keep numbering and naming stable across revisions
- preserve a predictable section sequence across modules

## Left Outline Navigation (Required)

Every module page must include:
- a left-side outline panel
- auto-generated navigable index from section headings
- active section highlighting while scrolling
- collapsible sidebar behavior (toggle open/close)
- collapsible tree controls with visible arrows/chevrons for expand/collapse of subsection groups
- click-to-navigate behavior for every index item

Implementation baseline:
- outline host in module layout (`#outline-nav`)
- behavior implemented by shared script (`site/assets/js/site.js`)

## Module Header Controls (Required)

Every module page must expose these controls in the header area:
- language selector (`#lang-select`)
- theme selector (`#theme-select`) with at least `light` and `dark`
- print button (top print trigger)

Every module page must also include:
- bottom print button (`#print-page-btn`)
- back-to-top button (`.top-link`)

## Figures Standard (Required)

Figures must follow the same behavior style used in the sibling project (`ai-ttt-course`):

- all figures are explicitly numbered (example: `Figure M3.2`)
- every figure is clickable
- click opens zoomed full-screen view (modal/lightbox style)
- second click (or close action) restores normal in-flow size
- figure caption always includes number + meaningful description
- image path must remain stable once module is finalized

Do not ship unnumbered instructional figures in finalized modules.

## Non-Regression Policy for Finalized Modules

Once a module is approved/finalized:

- key approved texts must not be removed
- approved images/figures must not disappear

Mandatory workflow:
1. Always run non-regression tests (`python3 scripts/non_regression_guard.py check`) **before** starting any modification to ensure a clean baseline.
2. Update/modify module content as needed.
3. Update/create lock file if the structure has intentionally changed  
   `python3 scripts/non_regression_guard.py lock site/chapters/chapter-XX.html --id Mx`
4. Run checks after every subsequent change to verify stability  
   `python3 scripts/non_regression_guard.py check`

Any failing lock check is a blocking regression until fixed.

## Editing Protocol

Work strictly module-by-module:

1. implement/update module content
2. review layout, links, outline behavior, and figure interactions
3. finalize module
4. lock module for non-regression
5. move to next module

Never silently rewrite previously finalized module content.

## Content Extraction and Writing Constraints (Required)

Source usage policy:
- source material and figures are extracted from `resources/`
- extracted module content must remain in English

Writing constraints:
- never reference the book directly
- do not preserve or mirror source/book section numbering; use course numbering only
- never reference a previous or following chapter/module
- use non-conversational, expository language
- keep content synthetic but readable (no excessive summarization)

Authoring workflow constraints:
- work one module at a time
- proceed step-by-step
- add figures and content only when explicitly requested by the user

## Code Links in Chapters (Required)

Chapters that cite implementation code from the companion repo link to specific lines on GitHub (see M10 §6-7 for the pattern: a `<p class="code-ref">` paragraph at the end of the section).

Rules:
- use permalinks pinned to a commit SHA (`.../blob/<sha>/chNN/file.py#Lx-Ly`), never a branch name, and only commits already pushed
- **whenever code in the companion repo is moved, renamed, or edited so that cited lines shift, update every affected link** (new SHA and line ranges) in the same working session
- verify before finishing a content change: `grep -rn "building-llm-applications/blob" site/chapters` and open each cited range at the pinned SHA (or `git show <sha>:path | sed -n 'a,bp'`) to confirm it still shows the named function
- after updating links, re-run the non-regression `lock` and `check`

## Lab Snippets File (Required)

The project uses `snippets-agents_v1.txt` as the live classroom execution file.

This file is intentionally flat:
- one command per line
- copy/paste ready for terminal execution
- minimal headings for grouping only (example: `## Esercizio 1: Prompt`)
- no long explanations inside the snippet body

Maintenance rules:
- update snippets incrementally while modules evolve
- keep ordering deterministic for live delivery
- prefer additive updates; avoid rewriting already validated command blocks
- when an exercise is finalized, preserve its snippet block unless an explicit change is approved

## Publishing (ITECH OnDemand)

The site is no longer deployed to Netlify. Publishing to ITECH OnDemand is done from Codex with the global skill:
- `/home/thimoty/.codex/skills/ondemand-course-publish/SKILL.md` (skill name: `ondemand-course-publish`)

Rules:
- this repository is the canonical source; a Git push does not update OnDemand by itself
- static publish directory is `site/`
- Claude Code commits and pushes only; the publish step is run by the user in Codex
- `netlify.toml`, `scripts/deploy_netlify.sh` and `skills/netlify-deploy/` are obsolete and kept only for reference
