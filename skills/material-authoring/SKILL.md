---
name: material-authoring
description: Author and update module content for agents-course with strict structure and UI rules.
---

# Material Authoring Skill

Use this skill when writing or revising module content for `agents-course`.

## Required Content Structure

- Work section-by-section and subsection-by-subsection.
- Use exactly two levels: section `x` and subsection `x.y`.
- Number all sections and subsections explicitly.
- Each subsection must be rendered in its own slide-like rectangular block.

## Required Navigation Behavior

- Keep a left navigation sidebar with the module outline.
- Sidebar must be collapsible.
- Every item in the sidebar must be clickable and navigate to the matching section/subsection.
- Sidebar structure must match page content structure (`h2`/`h3`) 1:1.

## Required Figure Behavior

- Number every figure.
- Every figure must be clickable.
- Click must open full-screen zoom.
- Click again (or close action) must restore normal size.

## Delivery Constraints

- Keep approved finalized text and images stable.
- Respect non-regression workflow before deploy.
- Apply updates incrementally, module by module.
