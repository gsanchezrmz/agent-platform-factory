---
scope: "global"
audience: "AI Coding Agents (Copilot, Cursor, Claude, etc.)"
---

# Rule: Artifact Evolution and Reuse

You are operating within the **Platform Engineering Layer** of an Agent Engineering Platform Factory.
When a human developer provides a new requirement (e.g., "Add a Data Quality Agent" or "Investigate SQL inactive configs"), you MUST NOT immediately write code or generate new files.

You must follow this deterministic 16-step reasoning process to determine how to evolve the platform:

## The 16-Step Agent Engineering Process

1.  **Understand the requirement:** What is the user trying to achieve?
2.  **Map the E2E Topology (MANDATORY):** Before proposing any Domain Agent or Tool, you MUST map the requirement against `docs/architecture/e2e-topology-template.md`. You must identify the State, Configuration (Control Plane), External Dependencies, Shared Infrastructure, and Telemetry dimensions.
3.  **Inspect existing Agents:** Look in `agents/`. Does an agent already exist for this domain?
4.  **Inspect existing Workflows:** Look in `workflows/`. Is there a workflow that can be adapted?
5.  **Inspect existing Skills:** Look in `skills/`. Do we already have the domain knowledge?
6.  **Verify Positive Heartbeats:** Check if the existing Skills only look for the *absence of errors*. You MUST ensure proposed Skills define "healthy" as *positive proof of work* (e.g., throughput > 0, recent timestamps), effectively countering Zombie states.
7.  **Evaluate Environmental Correlation:** Are failures potentially caused by noisy neighbors on shared infrastructure? Proposed Skills must account for cross-tenant/cross-pipeline correlation, not just isolated pipeline metrics.
8.  **Inspect existing Rules/Policies:** Look in `rules/` and `policies/`. Are there existing constraints we must follow?
9.  **Inspect existing Tools/MCP capabilities:** Look in `tools/` and `mcp/`. Do we have the infrastructure to query the required systems?
10. **Inspect existing Evaluations:** Look in `evaluations/`. How is this domain tested?
11. **Determine what is already covered:** Map existing artifacts to the requirement.
12. **Identify gaps:** What is missing? (Is it knowledge? A tool? A workflow step? Control plane visibility?)
13. **Determine the action for each gap:** You must classify the required change into one of the following categories:
    *   **REUSE:** Use an existing artifact unchanged.
    *   **EXTEND:** Modify an existing artifact because the new requirement exposes a missing capability within its current scope.
    *   **COMPOSE:** Combine existing Skills/Workflows to satisfy the new requirement.
    *   **NEW:** Create a new artifact because the capability represents a completely new domain or boundary.
    *   **INFRASTRUCTURE GAP:** The Agent Engineering artifact exists conceptually, but a Tool or MCP server is missing in `tools/` or `mcp/`.
    *   **EVALUATION GAP:** The capability exists, but the new behavior lacks an evaluation in `evaluations/`.
14. **Identify missing information:** Do you need credentials? Target system details? Clarification on logic?
15. **Ask the developer for clarification:** Present your questions explicitly.
16. **Propose the architecture and required changes:** Present a design document or plan.
17. **WAIT FOR APPROVAL:** Only after the developer approves the proposal should you implement the changes in the repository.

## Golden Rule of Platform Evolution
Do not assume that every new requirement requires a new Skill. Evaluate REUSE and COMPOSE before resorting to NEW.
