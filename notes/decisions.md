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
