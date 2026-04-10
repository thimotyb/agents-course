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
- avoid flat, unstructured content blocks
- keep numbering and naming stable across revisions
- preserve a predictable section sequence across modules

## Left Outline Navigation (Required)

Every module page must include:
- a left-side outline panel
- auto-generated navigable index from section headings
- active section highlighting while scrolling

Implementation baseline:
- outline host in module layout (`#outline-nav`)
- behavior implemented by shared script (`site/assets/js/site.js`)

## Figures Standard (Required)

Figures must follow the same behavior style used in the sibling project (`ai-ttt-course`):

- all figures are explicitly numbered (example: `Figure M3.2`)
- every figure is clickable
- click opens zoomed view (modal/lightbox style)
- figure caption always includes number + meaningful description
- image path must remain stable once module is finalized

Do not ship unnumbered instructional figures in finalized modules.

## Non-Regression Policy for Finalized Modules

Once a module is approved/finalized:

- key approved texts must not be removed
- approved images/figures must not disappear

Mandatory workflow:
1. finalize module content
2. create/update lock file  
   `python3 scripts/non_regression_guard.py lock site/chapters/chapter-XX.html --id Mx`
3. run checks after every subsequent change  
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
