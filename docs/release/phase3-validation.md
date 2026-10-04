# Phase 3 Validation Tests

## 1. Clone-and-Understand Test
**Objective:** Can a fresh AI engineer understand the repository without the Phase 4 Python runtime?

*   **What the platform is:** Clearly explained in `README.md` as an artifact-driven framework.
*   **What an Agent/Skill/Workflow/Rule/Policy is:** Defined in `README.md` and demonstrated with real files in `agents/`, `skills/`, etc.
*   **Relationships & Composition:** `README.md` and the frontmatter of `agents/replication_agent.md` show exactly how the Agent binds to Workflows, Skills, Tools, and Policies.
*   **How to create a new Agent/Skill:** Explicit, step-by-step instructions are in the `README.md`.
*   **Security constraints:** Explained in `README.md` and enforced via `policies/replication-read-only-policy.yaml`.
*   **Replication Agent structure:** fully realized with `replication_agent.md`, `replication-investigation-workflow.yaml`, and 4 highly detailed Markdown skills.
*   **Data Quality Agent reuse:** Covered in the README's "How to Create a New Agent" section, showing that no platform infrastructure needs to be duplicated.

**Result:** PASS. The repository is coherent and self-explanatory.

## 2. New-Agent Test (Data Quality Agent)
**Objective:** Verify that the repository provides enough structure for an AI engineer to create a Data Quality Agent.

**Simulated Process:**
1.  Read `README.md` and `AGENTS.md`.
2.  Understand that I need to create `agents/data_quality_agent.md`.
3.  Look at `agents/replication_agent.md` as a template for frontmatter (skills, workflows, tools).
4.  Write Data Quality specific skills in `skills/analyze_nulls.md`.
5.  Look at `rules/investigation-fact-vs-inference.md` and realize I need to append `data-quality-agent` to the `agents:` array in its frontmatter to apply the rule.
6.  Look at `policies/` and realize I can reuse or duplicate the read-only policy for the new agent.

**Result:** PASS. The AI engineer has all the structural examples and documentation needed to build the Data Quality Agent without touching a single Python file.

## 3. Conceptual Portability Test
**Objective:** Does the repository communicate the Agent Engineering model *without* running Python code?

**Result:** PASS. The knowledge (e.g., how to interpret Kafka lag) is stored in Markdown (`skills/analyze-kafka-lag.md`), the workflows are YAML, and the configuration is explicit. Any agent framework (Claude, Codex, custom harness) can parse these text files to understand the intended behavior. The domain knowledge is completely portable and decoupled from the execution engine.
