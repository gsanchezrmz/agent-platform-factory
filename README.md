# Data Platform Agent Engineering Platform

Welcome to the Data Platform Agent Engineering Platform. This repository provides the foundation for building, orchestrating, and governing autonomous AI agents specialized in Data Platform Engineering tasks (such as Replication Monitoring and Data Quality).

This platform is heavily inspired by the architectural philosophy of Everything Claude Code (ECC).

## What is this platform?
It is a **declarative, artifact-driven Agent Engineering Platform**.
Instead of hardcoding agents into monolithic Python applications, we define the *behavior, skills, workflows, and policies* of our agents as explicit, human-readable artifacts (Markdown, YAML, JSON).

The underlying Platform Runtime (implemented in Python in Phase 4) dynamically loads these artifacts, enforces deterministic security policies, and connects to external domain systems via the Model Context Protocol (MCP) or explicit tools.

## Architecture & Composition
The platform relies on the composition of specific artifacts:
*   **Agents (`agents/`)**: The core identity. An agent definition (Markdown + YAML) declares its persona, the skills it knows, the workflows it can run, and the tools/MCP servers it is allowed to access.
*   **Skills (`skills/`)**: Procedural knowledge. Written in Markdown, skills teach the LLM *how* to analyze data, what to look for, and how to format outputs.
*   **Workflows (`workflows/`)**: YAML files defining step-by-step orchestration logic that the agent must follow.
*   **Rules & Policies (`rules/`, `policies/`)**: Rules are engineering standards (Markdown) injected into the LLM context. Policies (YAML) are strict, deterministic security boundaries enforced by the runtime.
*   **Tools & MCP (`tools/`, `mcp/`)**: Definitions of the actual code capabilities the agent can invoke to interact with domain systems (e.g., NiFi, Kafka, Databricks).

### Example Composition
`replication_agent.md` uses the `replication-investigation-workflow.yaml`, which invokes the `collect-replication-evidence.md` skill, which relies on `get_kafka_lag.yaml` (a tool backed by `replication-mcp-config.json`).

## How to Create a New Agent (e.g., Data Quality Agent)
Because the platform is artifact-driven, adding a new Agent requires *no changes* to the core platform runtime.

1.  **Define the Agent:** Create `agents/data_quality_agent.md` outlining its purpose, bindings to skills, and allowed tools.
2.  **Teach it Skills:** Create new Markdown files in `skills/` (e.g., `skills/analyze_null_distributions.md`, `skills/investigate_schema_drift.md`). Define *when* to use them and *how* to interpret the results.
3.  **Define the Workflow:** Create `workflows/data_quality_triage.yaml` detailing the sequence of investigation.
4.  **Expose Tools:** Create tool definitions in `tools/` and configure any necessary external MCP servers in `mcp/` to allow the agent to query the data warehouse.
5.  **Secure it:** Apply or create policies in `policies/` ensuring the agent operates within safe, read-only bounds (for MVP).

## Security & Constraints
*   **Read-Only:** The current platform policy strictly enforces READ ONLY operations. No agent can mutate state or restart systems.
*   **Fact vs. Inference:** Agents are governed by `rules/investigation-fact-vs-inference.md`, forcing them to distinguish between raw tool data [FACT] and LLM reasoning [INFERENCE].
*   **Deterministic Policies:** Security is enforced outside the LLM. The `policies/` YAML files dictate what tools can be executed.

## Directory Structure
*   `agents/`: Agent definitions.
*   `skills/`: Reusable procedural knowledge.
*   `workflows/`: Declarative orchestration logic.
*   `rules/`: Engineering standards for the LLM.
*   `policies/`: Deterministic security constraints.
*   `tools/`: Declarative schemas for capabilities.
*   `mcp/`: Server configurations.
*   `evaluations/`: Test scenarios.
*   `platform/`: (Phase 4+) Reusable Python runtime execution machinery.
*   `domain/`: (Phase 4+) Domain-specific mock implementations and adapters.

*Note: This repository currently represents the Phase 3 Scaffold and Agent Engineering Artifacts. The Python Platform Runtime (Phase 4) is pending implementation.*
