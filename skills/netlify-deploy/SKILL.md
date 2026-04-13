---
name: netlify-deploy
description: Deploy the agents-course static site to Netlify using the same account credentials and operational settings used for ai-ttt-course.
---

# Netlify Deploy Skill

Use this skill when the user asks to deploy or publish the course site to Netlify.

## Goal

Deploy `site/` to Netlify in production mode, using:
- the same Netlify account credentials already used for `ai-ttt-course`
- the same static-site deploy approach (`publish = "site"`)

## Preconditions

- `NETLIFY_AUTH_TOKEN` is available in environment
- `NETLIFY_SITE_ID` points to the target Netlify site
- project root contains `netlify.toml` with `publish = "site"`

## Mandatory pre-deploy gate

Before deploying, run and pass:

```bash
python3 scripts/non_regression_guard.py check
```

## Command

From project root:

```bash
scripts/deploy_netlify.sh "optional deploy message"
```

## Expected Behavior

- deploy source directory: `site/`
- deployment mode: production (`--prod`)
- authentication: token-based (`NETLIFY_AUTH_TOKEN`)
- target site: explicit (`NETLIFY_SITE_ID`)

## Troubleshooting

- If auth fails: verify token is still valid for the same Netlify account used in `ai-ttt-course`.
- If site is wrong: verify `NETLIFY_SITE_ID` before running deploy.
- If command not found: script uses `npx netlify-cli`, no global install required.
