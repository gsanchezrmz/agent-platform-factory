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

2.  **Analyze Dependencies:**
    *   Before proposing a new Skill, check if the required Tool/MCP capability exists in `tools/` or `mcp/`. If it doesn't, you must flag an **INFRASTRUCTURE GAP**.

3.  **Drafting the Proposal:**
    When asked to build a new agent, format your proposal as follows:
    *   **Proposed Agent:** (Name and location)
    *   **Workflows (REUSE/NEW):** (List workflows to reuse or create)
    *   **Skills (REUSE/EXTEND/NEW):** (List skills, e.g., "REUSE: analyze-kafka-lag, NEW: check-sql-config")
    *   **Tools/MCP (GAPS):** (Identify what infrastructure adapters are required)
    *   **Policies:** (Identify which policies apply, usually read-only for MVPs)

## Example Scenario: SQL Config Investigation
If a user asks: *"Investigate Kafka topics not receiving data because the SQL config is inactive."*
1.  **Inspect:** You see `analyze-kafka-lag.md` exists.
2.  **Gap:** You lack a skill to check SQL configs, and a tool to query SQL.
3.  **Action:** Propose extending the `replication-investigation-workflow.yaml`, creating a NEW skill `analyze-sql-replication-config.md`, and flagging an INFRASTRUCTURE GAP for a `get_sql_record` tool.
