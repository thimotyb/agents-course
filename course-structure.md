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
| M3 | RAG Systems | `site/chapters/chapter-03.html` | O'Reilly book contents (Ch 06) | Foundational RAG pipeline |
| M4 | Advanced RAG | `site/chapters/chapter-04.html` | O'Reilly book contents + advanced retrieval/evaluation chapters | Query strategies, reranking, eval |
| M5 | AI Agents Architectures with LangGraph | `site/chapters/chapter-05.html` | O'Reilly book contents + agent architecture chapters | Multi-step, tools, memory, control flow |
| M6 | Google Agent Development Kit | `site/chapters/chapter-06.html` | Official ADK documentation + Google Codelab: AI Agents On-Ramp | ADK-based agent implementation and operations |
| M7 | Labs and Exercises from Building LLM Applications | `site/chapters/chapter-07.html` | `building-llm-applications` repository | Practical implementation module with guided labs and exercises |
| M8 | Agent Architectures: Foundational Patterns and Strategies | `site/chapters/chapter-08.html` | Claude Certified Architect - Foundations study guide and Exam Guide | Certification-informed foundations for agent loops, orchestration, tools, workflows, prompts, and reliability |

## Source Inventory

| Source File | Type | Used In Modules | Notes |
| --- | --- | --- | --- |
| `https://learning.oreilly.com/library/view/ai-agents-and/9781633436541/Text/contents.html` | book table of contents | `M1, M2, M3, M4, M5` | Canonical source for module progression |
| `https://adk.dev/get-started/` | official documentation | `M6` | Primary ADK onboarding reference |
| `https://codelabs.developers.google.com/onramp/instructions?hl=it#0` | official Google Codelab | `M6` | Base source for the final ADK course module and its guided practical path |
| `https://www.skills.google/catalog?format%5B%5D=labs&keywords=Agent+Development+Kit` | official Google Skills catalog | `M6` | Source for the compact two-lab ADK sequence, durations, levels, stable links, and credit planning |
| `https://github.com/BerriAI/litellm` | open-source model gateway/library | `M6` | Reference for routing a common model interface to Ollama, DeepSeek, and other providers through the ADK LiteLLM adapter |
| `https://github.com/thimotyb/building-llm-applications.git` | source repository | `M7` | Canonical source for labs and exercises |
| `https://claudecertificationguide.com/learn/` | public certification curriculum | `M8` | Task statements and learning examples across Agentic Architecture, Tool Design and MCP, Claude Code, Prompt Engineering, and Context Management |
| `https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf` | certification exam guide (PDF) | `M8` | Blueprint, domain weights, scenario patterns, in-scope concepts, and implementation trade-offs |
| `resources/` | local supporting assets | `M1, M2, M3, M4, M5, M6, M7` | Labs, slides, notebooks, diagrams to be added incrementally |

## Mapping Rules

- Keep one module page per module under `site/chapters/`.
- Keep module code stable (`M1` to `M8`) for the whole project lifecycle.
- Update this file whenever modules are split, merged, or renamed.
- Add every new source explicitly in Source Inventory.
