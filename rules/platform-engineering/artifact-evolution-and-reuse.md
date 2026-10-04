---
scope: "global"
audience: "AI Coding Agents (Copilot, Cursor, Claude, etc.)"
---

# Rule: Artifact Evolution and Reuse

You are operating within the **Platform Engineering Layer** of an Agent Engineering Platform Factory.
When a human developer provides a new requirement (e.g., "Add a Data Quality Agent" or "Investigate SQL inactive configs"), you MUST NOT immediately write code or generate new files.

You must follow this deterministic 14-step reasoning process to determine how to evolve the platform:

## The 14-Step Agent Engineering Process

1.  **Understand the requirement:** What is the user trying to achieve?
2.  **Inspect existing Agents:** Look in `agents/`. Does an agent already exist for this domain?
3.  **Inspect existing Workflows:** Look in `workflows/`. Is there a workflow that can be adapted?
4.  **Inspect existing Skills:** Look in `skills/`. Do we already have the domain knowledge?
5.  **Inspect existing Rules/Policies:** Look in `rules/` and `policies/`. Are there existing constraints we must follow?
6.  **Inspect existing Tools/MCP capabilities:** Look in `tools/` and `mcp/`. Do we have the infrastructure to query the required systems?
7.  **Inspect existing Evaluations:** Look in `evaluations/`. How is this domain tested?
8.  **Determine what is already covered:** Map existing artifacts to the requirement.
9.  **Identify gaps:** What is missing? (Is it knowledge? A tool? A workflow step?)
10. **Determine the action for each gap:** You must classify the required change into one of the following categories:
    *   **REUSE:** Use an existing artifact unchanged.
    *   **EXTEND:** Modify an existing artifact because the new requirement exposes a missing capability within its current scope.
    *   **COMPOSE:** Combine existing Skills/Workflows to satisfy the new requirement.
    *   **NEW:** Create a new artifact because the capability represents a completely new domain or boundary.
    *   **INFRASTRUCTURE GAP:** The Agent Engineering artifact exists conceptually, but a Tool or MCP server is missing in `tools/` or `mcp/`.
    *   **EVALUATION GAP:** The capability exists, but the new behavior lacks an evaluation in `evaluations/`.
11. **Identify missing information:** Do you need credentials? Target system details? Clarification on logic?
12. **Ask the developer for clarification:** Present your questions explicitly.
13. **Propose the architecture and required changes:** Present a design document or plan.
14. **WAIT FOR APPROVAL:** Only after the developer approves the proposal should you implement the changes in the repository.

## Golden Rule of Platform Evolution
Do not assume that every new requirement requires a new Skill. Evaluate REUSE and COMPOSE before resorting to NEW.
