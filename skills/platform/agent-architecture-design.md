# Skill: Agent Architecture Design

This skill belongs to the **Platform Engineering Layer**. It teaches an AI coding harness (like you) how to architect a new Data Platform Agent.

## Purpose
To ensure that all new agents conform to the strict separation of concerns (Platform Runtime vs. Agent Artifacts vs. Domain) and use the declarative YAML/Markdown model correctly.

## When to use
* A developer asks you to "Create a new agent for [Domain]".
* A developer asks you to add a new investigation capability that spans multiple systems.

## Procedural Knowledge

1.  **Enforce Artifact Boundaries:**
    *   Never create a `.py` file to define an Agent, Skill, or Workflow.
    *   Agents MUST be `.md` files with YAML frontmatter in `agents/`.
    *   Skills MUST be `.md` files in `skills/`.
    *   Workflows MUST be `.yaml` files in `workflows/`.
    *   Policies MUST be `.yaml` files in `policies/`.

2.  **Topology & Control Plane Validation:**
    *   You MUST review the E2E Topology Map.
    *   If the map identifies a Control Plane (e.g., Configuration DB, Routing Rules), you MUST propose Tools/MCP servers to query that Control Plane. Flag an **INFRASTRUCTURE GAP** if they do not exist. Do not rely solely on Data Plane telemetry.

3.  **External Dependency Graph Validation:**
    *   If the topology identifies IAM, Secret, or Network dependencies, you MUST NOT assume errors are isolated to the application layer. Propose explicit Tools/Skills to verify the health of these external dependencies (e.g., check if a Service Principal is expired).

4.  **Shared Infrastructure (Noisy Neighbor) Validation:**
    *   If the topology identifies Shared Compute or Storage, you MUST design Skills that analyze system-wide telemetry (e.g., CPU credit exhaustion across the entire Databricks cluster), not just pipeline-specific logs.

5.  **Analyze Dependencies:**
    *   Before proposing a new Skill, check if the required Tool/MCP capability exists in `tools/` or `mcp/`. If it doesn't, you must flag an **INFRASTRUCTURE GAP**.

6.  **Drafting the Proposal:**
    When asked to build a new agent, format your proposal as follows:
    *   **Proposed Agent:** (Name and location)
    *   **Workflows (REUSE/NEW):** (List workflows to reuse or create)
    *   **Skills (REUSE/EXTEND/NEW):** (List skills, ensuring "Positive Heartbeats", "External Dependency", and "Shared Infrastructure" checks are included).
    *   **Tools/MCP (GAPS):** (Identify what infrastructure adapters are required, explicitly separating Control Plane vs Data Plane tools)
    *   **Policies:** (Identify which policies apply, usually read-only for MVPs)
