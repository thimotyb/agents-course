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
| M6 | Google Agent Development Kit | `site/chapters/chapter-06.html` | Official ADK documentation + Google Codelab: AI Agents On-Ramp + `building-llm-applications/ch12/adk` + `building-llm-applications/ch12/adk_graph_upgrade` | ADK implementation, graph data handling, LiteLLM model switching, and operations |
| M7 | Labs and Exercises from Building LLM Applications | `site/chapters/chapter-07.html` | `building-llm-applications` repository | Practical implementation module with guided labs and exercises |
| M8 | Agent Architectures: Foundational Patterns and Strategies | `site/chapters/chapter-08.html` | Claude Certified Architect - Foundations study guide and Exam Guide | Certification-informed foundations for agent loops, orchestration, tools, workflows, prompts, and reliability |
| M9 | Agent2Agent Protocol and Agent Deployment | `site/chapters/chapter-09.html` | A2A Protocol, ADK A2A guides, Google Agent Runtime, and MuleSoft Agent Fabric documentation | Interoperable agents, ADK server/client implementation, deployment choices, and enterprise agent networks |

## Source Inventory

| Source File | Type | Used In Modules | Notes |
| --- | --- | --- | --- |
| `https://learning.oreilly.com/library/view/ai-agents-and/9781633436541/Text/contents.html` | book table of contents | `M1, M2, M3, M4, M5` | Canonical source for module progression |
| `https://adk.dev/get-started/` | official documentation | `M6` | Primary ADK onboarding reference |
| `https://adk.dev/get-started/python/` | official ADK Python quickstart | `M6` | Installation, project creation, credentials, CLI execution, and local web development UI |
| `https://adk.dev/agents/llm-agents/` | official ADK simple agents documentation | `M6` | LlmAgent identity, instructions, tools, model configuration, context, schemas, planners, and code execution |
| `https://colab.research.google.com/drive/16YGY_eTLag6DbebAMj2QmXFwY0AU6Yg0` | instructor-provided Google Colab notebook | `M6` | ADK 1 exercise notebook 1, linked from section 2; access requires an authorized Google account |
| `https://colab.research.google.com/drive/1bIp_432a-FxabwdXG9T02sfcVmFjNO8o` | instructor-provided Google Colab notebook | `M6` | ADK 1 exercise notebook 2, linked from section 2; access requires an authorized Google account |
| `https://adk.dev/graphs/` | official ADK graph workflow documentation | `M6` | Graph-based workflows, node and edge composition, routing, typed data flow, and workflow limitations |
| `https://adk.dev/graphs/data-handling/` | official ADK graph data handling documentation | `M6` | Event outputs, user-facing messages, routing data, session state scopes, schema-constrained structured data, and agent access to graph data |
| `https://adk.dev/graphs/dynamic/` | official ADK dynamic workflow documentation | `M6` | Programmatic orchestration, runtime branching, checkpointing, resume behavior, and dynamic data flow |
| `https://adk.dev/workflows/collaboration/` | official ADK collaborative workflows documentation | `M6` | Coordinator and subagent teams, collaboration modes, control transfer, context isolation, and limitations |
| `https://adk.dev/workflows/patterns/` | official ADK workflow patterns documentation | `M6` | Coordinator, sequential, parallel, hierarchical, generate-review, iterative refinement, and human-in-the-loop patterns |
| `https://codelabs.developers.google.com/onramp/instructions?hl=it#0` | official Google Codelab | `M6` | Base source for the final ADK course module and its guided practical path |
| `https://www.skills.google/catalog?format%5B%5D=labs&keywords=Agent+Development+Kit` | official Google Skills catalog | `M6` | Source for the compact ADK lab sequence, durations, levels, stable links, and credit planning |
| `https://www.skills.google/focuses/104687` | official Google Skills lab | `M6` | Additional ADK lab supplied for the M6 guided learning sequence; confirm title, duration, and credits in the catalog |
| `https://www.skills.google/focuses/137365` | official Google Skills lab | `M6` | Required public lab, available without GEAR enrollment. Build Multi-Agent Systems with ADK (GENAI106) provides ADK 2 examples for hierarchical multi-agent teams, session state, and sequential, loop, and parallel workflow agents; advanced, 90 minutes, and listed at 7 credits when verified |
| `https://www.skills.google/focuses/132170` | official Google Skills lab | `M6` | Connect to Remote Agents with ADK and the Agent2Agent (A2A) SDK (GENAI120): advanced 90-minute lab covering A2A servers, Agent Cards, remote-agent discovery, and ADK sub-agent integration; listed at 7 credits when verified |
| `https://www.skills.google/focuses/132178` | official Google Skills lab | `M6` | Use Model Context Protocol (MCP) Tools with ADK Agents (GENAI124): advanced 90-minute lab using Google Maps MCP tools and a custom MCP server; listed at 7 credits when verified, but currently access-restricted or unavailable for some accounts |
| `https://www.skills.google/focuses/125062` | official Google Skills lab | `M6` | Deploy ADK agents to Agent Runtime (GENAI107): advanced 90-minute lab covering ADK CLI deployment, querying, monitoring, and deletion in the managed Agent Runtime; listed at 5 credits when verified |
| `https://github.com/BerriAI/litellm` | open-source model gateway/library | `M6` | Reference for routing a common model interface to Ollama, DeepSeek, and other providers through the ADK LiteLLM adapter |
| `https://adk.dev/agents/models/litellm/` | official ADK model documentation | `M6` | LiteLLM connector and <code>LiteLlm</code> wrapper for non-Gemini models |
| `https://adk.dev/agents/models/ollama/` | official ADK model documentation | `M6` | Local Ollama model connection via LiteLLM |
| `https://github.com/thimotyb/building-llm-applications/tree/feat/deepseek-4-support/ch12/adk` | runnable ADK exercise | `M6` | Budget day-trip advisor with DeepSeek/Ollama switch, DuckDuckGo search, Open-Meteo forecast, and ADK Web instructions |
| `https://github.com/thimotyb/building-llm-applications/tree/feat/deepseek-4-support/ch12/adk_graph_upgrade` | runnable ADK 2 graph exercise | `M6` | Implementation of the flight-upgrade graph: mile thresholds, human consent, flight-history tool, local-Ollama analysis, conditional routing, and terminal upgrade or denial |
| `https://github.com/thimotyb/building-llm-applications.git` | source repository | `M7` | Canonical source for labs and exercises |
| `https://claudecertificationguide.com/learn/` | public certification curriculum | `M8` | Task statements and learning examples across Agentic Architecture, Tool Design and MCP, Claude Code, Prompt Engineering, and Context Management |
| `https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf` | certification exam guide (PDF) | `M8` | Blueprint, domain weights, scenario patterns, in-scope concepts, and implementation trade-offs |
| `https://a2a-protocol.org/latest/` | official A2A Protocol documentation | `M9` | Protocol purpose, interoperability, relationship with MCP, core actors, Agent Cards, messages, tasks, artifacts, and interaction modes |
| `https://adk.dev/a2a/` | official ADK A2A documentation | `M9` | ADK support for exposing and consuming A2A-compatible agents |
| `https://adk.dev/a2a/quickstart-exposing/` | official ADK Python guide | `M9` | Exposing an ADK agent with `to_a2a()`, generated Agent Cards, A2A request handling, and Uvicorn |
| `https://adk.dev/a2a/quickstart-consuming/` | official ADK Python guide | `M9` | Discovering and consuming an A2A service with `RemoteA2aAgent` |
| `https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime?hl=it` | official Google Cloud documentation | `M9` | Managed Agent Runtime lifecycle, supported deployment inputs, security, scaling, querying, and operations |
| `https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/intro_agent_engine.ipynb?hl=it` | official Google Cloud Colab notebook | `M9` | Guided Agent Runtime setup, deployment, remote invocation, management, and cleanup |
| `https://docs.mulesoft.com/agent-network/latest/af-agent-networks` | official MuleSoft documentation | `M9` | Agent Fabric networks, guided determinism, A2A agents, MCP servers, Exchange, CloudHub 2.0, Omni Gateway, and observability |
| `building-llm-applications/ch13` | runnable ADK A2A exercise | `M9` | Local-Ollama ADK server exposed with `to_a2a()` and ADK client consuming it through `RemoteA2aAgent` |
| `resources/` | local supporting assets | `M1, M2, M3, M4, M5, M6, M7, M8, M9` | Labs, slides, notebooks, diagrams to be added incrementally |

## Mapping Rules

- Keep one module page per module under `site/chapters/`.
- Keep module code stable (`M1` to `M9`) for the whole project lifecycle.
- Update this file whenever modules are split, merged, or renamed.
- Add every new source explicitly in Source Inventory.
