---
scope: "global"
audience: "AI Coding Agents (Copilot, Cursor, Claude, Gemini, Antigravity, etc.)"
---

# Rule: Artifact Evolution and Reuse

You are operating within the **Platform Engineering Layer** of the Agent Engineering Platform Factory.
When a human developer provides a new requirement (e.g., "Add an incident investigator", "Support SQL replication issues"), you MUST NOT immediately write code, hallucinate tools, or create standalone files.

You must follow this deterministic, context-aware 14-step reasoning process:

---

## The 14-Step Systemic Agent Engineering Process

### Phase 1: Environment & Context Discovery (Mandatory Step 0)
0. **Inspect and Verify E2E Topology:**
   * Look in `docs/architecture/` for the populated environment topology document (following `docs/architecture/e2e-topology-template.md`).
   * If missing or incomplete for the required domain, **STOP**. Interrogate the human developer for the End-to-End infrastructure, Control Planes (where configs live), and known deceptive states/failure modes. Populate or update the topology document BEFORE proceeding.
   * Never accept vague tech terms (e.g., "SQL", "cloud service") without mapping the exact engine, hosting, and configuration source.

### Phase 2: Systematic Repository Audit
1. **Understand the requirement:** What specific business or investigative outcome is desired?
2. **Inspect existing Agents:** Look in `agents/`. Does an agent already cover this domain or operational scope?
3. **Inspect existing Workflows:** Look in `workflows/`. Can an existing orchestration pipeline be adapted or composed?
4. **Inspect existing Skills:** Look in `skills/`. Do we already have procedural reasoning or technology references?
5. **Inspect existing Rules/Policies:** Look in `rules/` and `policies/`. What deterministic boundaries (e.g. read-only, fact-vs-inference) apply?
6. **Inspect existing Tools/MCP capabilities:** Look in `tools/` and `mcp/`. Do we have the declarative infrastructure to query every hop identified in the E2E topology?
7. **Inspect existing Evaluations:** Look in `evaluations/`. How is this domain tested, and what mock infrastructure exists?

### Phase 3: Gap Analysis & Action Mapping
8. **Determine what is already covered:** Map existing artifacts against the topology hops.
9. **Identify gaps across the 3 Component Dimensions:**
   * *State Gap:* Missing data payload visibility.
   * *Configuration Gap:* Missing inspection of control plane / settings that govern the node.
   * *Telemetry/Anomaly Gap:* Inability to detect deceptive or hung states.
10. **Classify action for each gap:**
    * **REUSE:** Use an existing artifact unchanged.
    * **EXTEND:** Broaden an existing artifact's scope when the requirement belongs to its domain.
    * **COMPOSE:** Chain existing Skills/Workflows together.
    * **NEW:** Create an artifact only when dealing with an unprecedented domain boundary.
    * **INFRASTRUCTURE GAP:** A declarative tool specification or MCP definition is missing in `tools/` or `mcp/`.
    * **EVALUATION GAP:** The capability lacks a synthetic incident scenario or validation suite in `evaluations/`.
    * **CONTEXT GAP:** An architectural node or configuration dependency exists in reality but is missing from the E2E topology document.

### Phase 4: Alignment, Proposal & Approval Gate
11. **Identify missing information:** Highlight unresolved infrastructure credentials, gateway protocols, or anomaly patterns.
12. **Ask the developer for clarification:** Present targeted, architectural questions.
13. **Propose the architecture and required changes:** Present a formal Agent Architecture Proposal detailing exact files, reuse justifications, and evaluation plans.
14. **WAIT FOR APPROVAL:** Do NOT create or modify implementation files until the developer formally approves the design proposal.

---

## The Incident-Driven Evolution Loop (Feedback Loop)

When a Domain Agent encounters an unhandled incident, silent failure, or misconfiguration in production:
1. **Never patch the agent directly.**
2. **First:** Update the E2E Topology with the newly discovered component configuration or failure mode.
3. **Second:** Run the 14-Step Process to systematically update the Tools, Skills, and Evaluation suites to cover that new failure mode permanently.

## Golden Rules of Platform Evolution
* **Golden Rule 1:** Evaluate REUSE and COMPOSE before resorting to NEW.
* **Golden Rule 2:** No component in an E2E pipeline is assumed to be configuration-free. Always inspect where its governing rules reside.
* **Golden Rule 3:** Telemetry can be deceptive. Never rely solely on OS service states when unstructured heartbeat logs exist.
