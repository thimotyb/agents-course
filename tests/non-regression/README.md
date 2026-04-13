# Non-regression Locks (Modules)

When a module is finalized, create a lock that freezes:
- required key texts
- required image references (`<img src=...>`)

Regression checks also enforce baseline module UI/structure on every
`site/chapters/chapter-*.html` page:
- print controls are present
- top button is present
- left outline navigation is present
- language selector is present
- theme selector is present
- content keeps a two-level heading hierarchy (`h2` + `h3`, no deeper levels)
- heading numbering is validated (no duplicates, sequential siblings, valid `h3` -> `h2` parent)

## Create or update a lock

```bash
cd /home/thimoty/git/agents-course
python3 scripts/non_regression_guard.py lock site/chapters/chapter-01.html --id M1
```

## Run checks

```bash
cd /home/thimoty/git/agents-course
python3 scripts/non_regression_guard.py check
```

Check one module only:

```bash
python3 scripts/non_regression_guard.py check --id M1
```

## Workflow

1. Complete module content.
2. Confirm module is final.
3. Run `lock` for that module.
4. Run `check` after every change (or in CI) to detect regressions.
