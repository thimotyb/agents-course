# Course Decisions

## Non-regression policy for finalized modules

When a module is finalized, it is treated as locked content.

From that point onward, every update must run non-regression checks to ensure:
- finalized key texts are still present
- finalized images are still present

Workflow:
1. Work module by module.
2. Finalize module content.
3. Create/update lock for that module.
4. Run non-regression checks after every change.

This policy prevents accidental drift of approved texts and images.

## Lab snippets operating mode

A dedicated file `snippets-agents_v1.txt` is used during live sessions.

Rules:
- keep snippets flat and execution-oriented
- one command per line, ready for copy/paste in terminal
- optionally group commands with headings like `## Esercizio X`
- avoid long explanations in the snippet file
- append snippets incrementally module by module

Purpose:
- guide learners step-by-step during setup and exercises
- reduce confusion during live execution
- keep a stable, reusable command sequence for labs

## Mandatory module UI and structure regression gates

Every module page must always keep:
- print controls (top print button and module print button)
- top/back-to-top button
- left outline navigation bar
- language selector
- theme selector

Structure constraints:
- content must keep two levels (`h2` + `h3`)
- heading structure must remain aligned with the left outline navigation

## Content extraction and editorial constraints

Operational decisions:
- source text and figures are extracted from files in `resources/`
- module content is always authored in English

Editorial decisions:
- never mention the book as a source in module prose
- never mention previous/next chapter or module references
- use expository and non-colloquial tone
- keep content concise and readable without over-summarizing

Execution workflow:
- proceed one module at a time
- proceed step-by-step
- add figures and content incrementally based on user instructions

## Project Progress Log

### 2026-04-15
- **M1:** Verified and locked. Fixed broken GitHub link in Guided Lab (underscore vs hyphen).
- **M2 (Summarization):**
    - Completed Section 3 (Multi-document summarization with MapReduce and Refine).
    - Completed Section 4 (Research Engine):
        - 4.1 Overview (Figures M2.6, M2.7).
        - 4.2 Core Components: Web Search & Scraping (Figure M2.8 - Debugger).
        - 4.3 Query Rewriting (Figure M2.9).
        - 4.4 Prompt Engineering (Modular prompts.py).
        - 4.5 Sequential Pipeline (Figure M2.10 - Execution log).
    - Updated Guided Lab with Ch03 and Ch04 GitHub links.
- **Infrastructure:**
    - Updated `non_regression_guard.py` with broken image detection and external GitHub link verification.
    - Added `non_regression_standards` and `course_authoring_skill` specifications to `mempalace.yaml`.
    - Synchronized workspace with centralized MemPalace database on Google Drive.
