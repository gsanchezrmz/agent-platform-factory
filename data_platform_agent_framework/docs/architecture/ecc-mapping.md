# ECC Concept Mapping for Data Platform Engineering

This document details how we adapted the organizational and composition philosophy of Everything Claude Code (ECC) to our Data Platform Agent Engineering Platform.

| ECC Concept | ECC Purpose | Data Platform Equivalent | Decision | Implementation Form |
| :--- | :--- | :--- | :--- | :--- |
| **Skills** | Reusable agent knowledge/capability | Data Platform Skills | **Adapt** | Declarative Markdown (`artifacts/skills/`). Holds heuristics and procedures. Not code. |
| **Agents** | Specialized agent behavior | Data Platform Agents | **Adapt** | Declarative YAML configuration (`artifacts/agents/`). Defines identity, purpose, and linked skills/workflows. |
| **Hooks** | Lifecycle/behavior controls | Agent Hooks | **Reject/Deferred** | For MVP, runtime handles lifecycle (e.g., policy checks before tools). Specific custom hooks are deferred to avoid over-engineering. |
| **Commands** | Reusable CLI operations | Domain Actions / Tools | **Reject** | We do not allow arbitrary commands. Replaced entirely by deterministic Tools via MCP. |
| **Rules** | Constraints/conventions | Policies/Guardrails | **Adapt** | Deterministic Python Engine (`platform/security/`). Must be out-of-band and non-bypassable by LLM. |
| **Workflows** | Multi-step procedures | Data Platform Workflows | **Adapt** | Declarative YAML defining sequences of tool invocations or reasoning steps (`artifacts/workflows/`). |
| **Tools** | Executable capabilities | Data Platform Tools | **Adopt** | Executable Python components wrapped via FastMCP abstractions (`domain/tools/` and `platform/integrations/mcp/`). |
| **Configuration** | Agent/project behavior | Platform Configuration | **Adopt** | YAML files (`artifacts/config/`). |

## Key Takeaway
We preserve the ECC principle that agent behavior is defined by composable artifacts (Skills, Workflows, Agent Configs). However, because we operate in a highly secure Data Platform, we use declarative YAML/Markdown rather than Python classes for these concepts, while Python implements the strict, deterministic execution runtime and policy engine.
