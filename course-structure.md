# Course Structure

- Course name: AI Agent Programming (LangChain + LangGraph)
- Audience: Developers and technical architects with Python basics
- Language: English primary; Italian via on-page Google Translate switch
- Output format: Static interactive course website
- Theme: Deep Ocean

## Modules

| Module | Title | Output Artifact | Source Files | Notes |
| --- | --- | --- | --- | --- |
| M1 | Getting Started with LLMs and LangChain | `site/chapters/chapter-01.html` | O'Reilly book contents + selected sections from Part 1 | Baseline concepts, setup, first chains |
| M2 | Summarization with LangChain and LangGraph | `site/chapters/chapter-02.html` | O'Reilly book contents + summarization-oriented chapters | Prompt compression and graph workflows |
| M3 | RAG Systems | `site/chapters/chapter-03.html` | O'Reilly book contents + retrieval-focused chapters | Foundational RAG pipeline |
| M4 | Advanced RAG | `site/chapters/chapter-04.html` | O'Reilly book contents + advanced retrieval/evaluation chapters | Query strategies, reranking, eval |
| M5 | AI Agents Architectures with LangGraph | `site/chapters/chapter-05.html` | O'Reilly book contents + agent architecture chapters | Multi-step, tools, memory, control flow |
| M6 | Google Agent Development Kit | `site/chapters/chapter-06.html` | ADK docs + guided tutorials | ADK-based agent implementation and operations |
| M7 | Labs and Exercises from Building LLM Applications | `site/chapters/chapter-07.html` | `building-llm-applications` repository | Practical implementation module with guided labs and exercises |

## Source Inventory

| Source File | Type | Used In Modules | Notes |
| --- | --- | --- | --- |
| `https://learning.oreilly.com/library/view/ai-agents-and/9781633436541/Text/contents.html` | book table of contents | `M1, M2, M3, M4, M5` | Canonical source for module progression |
| `https://adk.dev/get-started/` | official documentation | `M6` | Primary ADK onboarding reference |
| `https://github.com/thimotyb/building-llm-applications.git` | source repository | `M7` | Canonical source for labs and exercises |
| `resources/` | local supporting assets | `M1, M2, M3, M4, M5, M6, M7` | Labs, slides, notebooks, diagrams to be added incrementally |

## Mapping Rules

- Keep one module page per module under `site/chapters/`.
- Keep module code stable (`M1` to `M7`) for the whole project lifecycle.
- Update this file whenever modules are split, merged, or renamed.
- Add every new source explicitly in Source Inventory.
