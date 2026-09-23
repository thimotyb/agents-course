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
| `https://adk.dev/get-started/python/` | official ADK Python quickstart | `M6` | Installation, project creation, credentials, CLI execution, and local web development UI |
| `https://adk.dev/agents/llm-agents/` | official ADK simple agents documentation | `M6` | LlmAgent identity, instructions, tools, model configuration, context, schemas, planners, and code execution |
| `https://adk.dev/graphs/` | official ADK graph workflow documentation | `M6` | Graph-based workflows, node and edge composition, routing, typed data flow, and workflow limitations |
| `https://adk.dev/graphs/dynamic/` | official ADK dynamic workflow documentation | `M6` | Programmatic orchestration, runtime branching, checkpointing, resume behavior, and dynamic data flow |
| `https://adk.dev/workflows/collaboration/` | official ADK collaborative workflows documentation | `M6` | Coordinator and subagent teams, collaboration modes, control transfer, context isolation, and limitations |
| `https://adk.dev/workflows/patterns/` | official ADK workflow patterns documentation | `M6` | Coordinator, sequential, parallel, hierarchical, generate-review, iterative refinement, and human-in-the-loop patterns |
| `https://codelabs.developers.google.com/onramp/instructions?hl=it#0` | official Google Codelab | `M6` | Base source for the final ADK course module and its guided practical path |
| `https://www.skills.google/catalog?format%5B%5D=labs&keywords=Agent+Development+Kit` | official Google Skills catalog | `M6` | Source for the compact ADK lab sequence, durations, levels, stable links, and credit planning |
| `https://www.skills.google/focuses/104687` | official Google Skills lab | `M6` | Additional ADK lab supplied for the M6 guided learning sequence; confirm title, duration, and credits in the catalog |
| `https://www.skills.google/focuses/137365` | official Google Skills lab | `M6` | Required public lab, available without GEAR enrollment. Build Multi-Agent Systems with ADK (GENAI106) provides ADK 2 examples for hierarchical multi-agent teams, session state, and sequential, loop, and parallel workflow agents; advanced, 90 minutes, and listed at 7 credits when verified |
| `https://www.skills.google/focuses/132178` | official Google Skills lab | `M6` | Use Model Context Protocol (MCP) Tools with ADK Agents (GENAI124): advanced 90-minute lab using Google Maps MCP tools and a custom MCP server; listed at 7 credits when verified, but currently access-restricted or unavailable for some accounts |
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
