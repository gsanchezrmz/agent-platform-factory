# Baseline Agent Engineering Skills Architecture

## 1. Definition of Skill
A **Skill** is a reusable, AI-readable Agent Engineering artifact (Markdown) that provides procedural instructions, reasoning frameworks, and behavioral guidance to an AI Agent. It teaches an agent *how* to approach a specific type of task (e.g., "how to analyze logs" or "how to build an MCP server"). A Skill is NOT a software library, a Python class, an SDK, or executable code.

## 2. Definition of Reference Material
**Reference material** consists of detailed, factual, technology-specific documents (Markdown) that an AI Agent consumes when executing a Skill. If a Skill is the "verb" (the process), Reference material is the "noun" (the deep domain knowledge required to execute the process accurately).

## 3. Skill vs. Reference Distinction
*   **Skill:** Defines the universal procedure. (e.g., `skills/log-analysis/SKILL.md` -> Step 1: extract timestamp, Step 2: identify severity, Step 3: correlate).
*   **Reference:** Defines the technology-specific semantics. (e.g., `skills/log-analysis/reference/kafka_log_analysis.md` -> "A `RebalanceInProgress` error in Kafka indicates...").
*   *Why?* This prevents Skill bloat. We do not need a `kafka-skill` and a `nifi-skill`. We have one procedural Skill that references specific knowledge files based on the context.

## 4. Skill vs. Rule Distinction
*   **Skill:** Procedural and instructional ("Follow these steps to analyze a failure").
*   **Rule:** Mandatory constraints and engineering standards ("You must use `pytest`", "You must never state an inference as a fact"). Rules govern the bounds of behavior.

## 5. Skill vs. Tool Distinction
*   **Skill:** The cognitive process the LLM uses to decide what to do.
*   **Tool:** The executable capability (defined via YAML schema) the LLM calls to interact with the outside world (e.g., `get_databricks_pipeline_state`).

## 6. Skill vs. MCP Distinction
*   **Tool:** A single deterministic function.
*   **MCP (Model Context Protocol):** The standard integration protocol/server used to expose sets of Tools to the Agent securely, especially over enterprise boundaries.

## 7. Baseline Skills (Implemented)
We have established three foundational Platform Engineering Skills:
1.  **Development Best Practices (`skills/development-best-practices/SKILL.md`):** How to construct resilient Data Platform components.
2.  **MCP Development (`skills/mcp-development/SKILL.md`):** How to design, secure, and deploy MCP servers.
3.  **Log Analysis (`skills/log-analysis/SKILL.md`):** How to extract facts, timelines, and root causes from diagnostic text.

## 8. Reference Organization
Reference material is explicitly nested inside the skill it supports to maintain cohesion while avoiding skill bloat.
*   `skills/development-best-practices/reference/` (Python, C#, SQL)
*   `skills/mcp-development/reference/` (MCP Best Practices, Corporate Gateway)
*   `skills/log-analysis/reference/` (Generic, C#, SQL, NiFi, Kafka, Databricks, DLT)

## 9. Technology-Specific Reference Strategy
Instead of creating 10 different programming-language Skills, we created one `development-best-practices` Skill. When an AI is asked to write a Python component, the Skill instructs the AI to load `python_best_practices.md`. This ensures maintainability and high composability.

## 10. MCP Corporate Gateway Strategy
The `mcp-development` Skill dictates how to build schemas and handle errors. It explicitly instructs the AI to consult `reference/corporate-gateway.md` for strict guidance on handling TLS, authentication, rate limiting, and network boundaries without exposing real corporate secrets.

## 11. Log Analysis Strategy
We adopted the **Composed Generic Skill Pattern**.
One generic Skill (`log-analysis/SKILL.md`) defines the investigation loop (Extract -> Classify -> FACT vs INFERENCE). The AI is instructed to pull in `kafka_log_analysis.md` or `nifi_log_analysis.md` dynamically based on the telemetry source it is analyzing.

## 12. Development Best-Practices Strategy
The `development-best-practices` Skill guides the AI through the lifecycle of writing Data Platform code (Requirements -> Logic -> Error Handling -> Tests -> Observability). It relies on the reference material for the specific syntax and enterprise conventions of C#, SQL, or Python.

## 13. Metadata & Discovery Model
To allow AI harnesses (Copilot, Claude) to discover Skills without a Python runtime, we define a strict YAML frontmatter schema for `.md` files in `skills/`:
```yaml
name: log-analysis
description: "Universal procedure for extracting, structuring, and analyzing diagnostic evidence."
when_to_use: "When interpreting raw text logs or diagnostic payloads."
dependencies: ["skills/log-analysis/reference/..."]
```

## 14. Composition Model
**Scenario:** "Create a new C# MCP server to query a legacy SQL database."
1.  AI reads `skills/platform/agent-architecture-design.md` -> determines it needs to build an MCP.
2.  AI loads `skills/mcp-development/SKILL.md` (the process).
3.  AI loads `skills/development-best-practices/SKILL.md` (how to code).
4.  AI loads `reference/csharp_best_practices.md` and `reference/sql_best_practices.md` (the syntax/standards).
5.  AI loads `reference/corporate-gateway.md` (security constraints).
6.  AI loads `rules/*` (mandatory repo rules).
7.  AI generates the compliant codebase.

## 15. Platform vs. Domain Separation
*   **Platform (Baseline):** `log-analysis/SKILL.md`, `kafka_log_analysis.md`. These teach *how* to analyze logs or *what* Kafka is.
*   **Domain:** `agents/replication_agent.md`, `skills/correlate-replication-state.md`. These use the baseline capabilities to solve a specific business problem (Replication). Kafka reference material knows what a Kafka error is; the Replication skill knows what that error means for the business pipeline.

## 16. ECC Alignment
This architecture perfectly aligns with Everything Claude Code (ECC) and the Anthropic Skills repository. Knowledge is stored in human/AI-readable markdown files. Skills are explicit instructions, completely devoid of Python runtime framework constraints.

## 17. Multi-Harness Portability
Because Skills and References are pure Markdown and YAML, they are entirely agnostic to the underlying LLM. Copilot, Gemini, Codex, or Claude can load these text files into their context window and execute the procedures natively. No universal Python agent runtime adapter is required in Phase 3.

## 18. Replication Agent Example
When investigating a failure, the Replication Agent currently checks telemetry. Under this new architecture, it would:
1.  Call `get_kafka_logs` (Tool).
2.  Use `skills/log-analysis/SKILL.md` (Generic Baseline Skill).
3.  Load `kafka_log_analysis.md` (Reference Knowledge) to understand the error.
4.  Use `skills/correlate-replication-state.md` (Domain Skill) to declare the pipeline broken.
*Result: The generic log analysis logic is highly reusable and not hardcoded into the Replication Agent.*

## 19. Open Architectural Questions
*   How large can the combined Reference context grow before an AI harness exceeds its context window, requiring chunking or RAG? (Currently assumed small enough for direct context injection, but Databricks trace analysis can be highly verbose).
