# Clone and Use Test Report

## 1. Test Objective
The objective of this test is to determine if a completely fresh AI Coding Agent, without external historical context, can clone the repository, understand its architecture, and correctly utilize its Agent Engineering artifacts to analyze a new requirement (a Data Quality Agent).

## 2. Isolation Assumptions
I am operating under the strict assumption that I have zero prior knowledge of this repository's history, architectural debates, or conversations. My sole source of truth is the filesystem contents (Markdown, YAML, JSON).

## 3. Repository Understanding (First Test)

**A. What problem does this platform solve?**
It provides a declarative, portable foundation for building, evolving, and operating autonomous Data Platform Agents, decoupling the "what" (agent behavior) from the "how" (Python execution runtime or specific LLM harness).

**B. What is an Agent Engineering artifact?**
It is an explicit, inspectable, version-controlled definition that shapes AI behavior. It is represented in Markdown, YAML, or JSON, never as executable Python code.

**C. What types of artifacts exist currently?**
Agents, Skills, Workflows, Rules, Policies, Tools, MCP Configurations, and Evaluations.

**D. What is an Agent?**
The core identity. It is defined in Markdown (with YAML frontmatter) in `agents/`. It declares a persona, bound skills, workflows, tools, and MCP servers.

**E. What is a Workflow?**
A YAML file in `workflows/` that defines declarative, step-by-step orchestration logic that an agent must follow.

**F. What is a Skill?**
A reusable, procedural instruction (Markdown) that teaches an AI *how* to approach a task (e.g., how to analyze logs). It is the "verb".

**G. What is Reference material?**
Detailed, factual, technology-specific documents (Markdown) nested within a Skill's `reference/` directory. It is the "noun" that the Skill consults.

**H. What relationship exists between them?**
An Agent executes a Workflow. A Workflow orchestrates Skills. A Skill defines a procedure and delegates to Reference material for deep technical semantics.

**I. What role do Tools/MCP play?**
Tools (YAML) define the schemas for executable capabilities to interact with external systems. MCP (JSON) configures the standard integration protocol/servers that expose these Tools securely over the network boundary.

**J. What role do Rules/Policies play?**
Rules (Markdown) are engineering constraints (e.g., distinguish FACT vs INFERENCE). Policies (YAML) are strict, deterministic security boundaries (e.g., READ ONLY) enforced outside the LLM.

**K. What part corresponds to the Runtime?**
The Runtime (Phase 4, conceptually in `platform/` and `domain/`) is responsible for dynamically loading these artifacts, managing LLM sessions, and enforcing the Policies deterministically.

**L. What part does NOT belong to the Runtime?**
All declarative artifacts (Agents, Skills, Workflows, Rules, Policies, Tools, MCP, Evaluations) in their respective top-level directories.

**M. How does a Baseline Skill differ from a Domain Skill?**
A Baseline Skill (e.g., `log-analysis`) teaches reusable engineering procedures applicable across multiple agents. A Domain Skill (e.g., `correlate-replication-state`) uses baseline capabilities to solve a specific business problem for a specific agent.

## 4. Discovered Capabilities (Second Test)

### Baseline Agent Engineering Capabilities
1.  **Development Best Practices (`skills/development-best-practices/SKILL.md`):**
    *   *Purpose:* Guides the creation of robust Data Platform components.
    *   *When to use:* When writing or reviewing code.
    *   *Knowledge:* Lifecycle of coding (Requirements -> Logic -> Testing -> Observability).
    *   *References used:* `python_best_practices.md`, `csharp_best_practices.md`, `sql_best_practices.md`.
    *   *Consumers:* AI Coding Harnesses (Platform Engineering Layer).
2.  **MCP Development (`skills/mcp-development/SKILL.md`):**
    *   *Purpose:* Process for designing secure MCP servers.
    *   *When to use:* When building new infrastructure integrations.
    *   *Knowledge:* Capability assessment, schema design, security boundaries.
    *   *References used:* `mcp_best_practices.md`, `corporate-gateway.md`.
    *   *Consumers:* AI Coding Harnesses.
3.  **Log Analysis (`skills/log-analysis/SKILL.md`):**
    *   *Purpose:* Procedure for extracting facts from logs.
    *   *When to use:* When interpreting diagnostic text from tools.
    *   *Knowledge:* Evidence extraction, classification, FACT vs INFERENCE.
    *   *References used:* `generic_log_analysis.md`, `csharp_log_analysis.md`, `sql_error_analysis.md`, `kafka_log_analysis.md`, etc.
    *   *Consumers:* Domain Agents (e.g., Replication Agent).

### Domain Capabilities
1.  **Collect Replication Evidence (`skills/collect-replication-evidence/SKILL.md`):**
    *   *Problem:* Standardizes telemetry gathering across Hangfire, NiFi, Kafka, Databricks.
    *   *Agent/Workflow:* Used by `replication-monitoring-agent` in `replication-investigation-workflow.yaml`.
    *   *Reused baseline:* N/A (Purely domain orchestration of tools).
2.  **Correlate Replication State (`skills/correlate-replication-state/SKILL.md`):**
    *   *Problem:* Synthesizes the evidence matrix into a single Root Cause.
    *   *Agent/Workflow:* Used by `replication-monitoring-agent` in `replication-investigation-workflow.yaml`.
    *   *Reused baseline:* N/A.

### Existing Agent Analysis: Replication Monitoring & Investigation Agent
*   *Purpose / Problem:* Ensure health of data replication pipelines across source, transport, and processing layers.
*   *Workflow:* `replication-investigation-workflow`
*   *Skills:* `collect-replication-evidence`, `log-analysis`, `correlate-replication-state`
*   *References:* Inherits all references from `log-analysis`.
*   *Tools/MCP:* `get_nifi_processor_status`, `get_kafka_lag`, `get_hangfire_job_status`, `get_databricks_pipeline_state` (backed by mock MCPs).
*   *Policies/Rules:* `replication-read-only-policy`, `investigation-fact-vs-inference.md`
*   *Read-only capabilities:* All bound tools are READ ONLY.
*   *Missing capabilities:* None identified for its current narrow MVP scope. *(Note: The `evaluations/replication-incident-eval.yaml` contains an outdated reference to an `analyze-kafka-lag` skill which was pruned from the repo, showing a minor artifact drift).*

## 5. Data Quality Agent Analysis (Third Test)
**Requirement:** “We need to create a Data Quality Agent that investigates data quality incidents across the Data Platform."

### Analysis before Proposing
1.  *Existing Agent:* No. `replication_agent` is domain-specific.
2.  *Reusable Workflow:* No. `replication-investigation-workflow` is highly specific to replication layers.
3.  *Relevant Baseline Skills:* `log-analysis` (if DQ checks generate errors/logs).
4.  *Reusable Domain Skills:* None. DQ is a different domain than Replication.
5.  *Relevant References:* `sql_error_analysis.md` (highly relevant for DQ queries), `databricks_pipeline_analysis.md` (relevant for DLT Expectations).
6.  *Rules/Policies:* `investigation-fact-vs-inference.md` (applicable), `replication-read-only-policy.yaml` (needs a generic or DQ-specific read-only policy).
7.  *Tools/MCP:* `get_databricks_pipeline_state` might be reused. Missing tools to query actual data tables or DQ metrics.
8.  *Evaluations:* None reusable.
9.  *Gaps:* Agent definition, DQ Workflow, DQ-specific skills (e.g., `analyze-null-distribution`), Tools to query data warehouses.

## 6. Reuse / Compose / Extend / New Decisions
*   `log-analysis/SKILL.md`: **REUSE**. Will be used to interpret any errors returned during DQ checks.
*   `investigation-fact-vs-inference.md`: **EXTEND**. Modify the frontmatter `agents:` array to include the new Data Quality Agent.
*   `replication-read-only-policy.yaml`: **NEW ARTIFACT**. Create `data-quality-read-only-policy.yaml`. (It is bad practice to bind a "replication" named policy to a DQ agent, even if the rules are identical).
*   `data_quality_agent.md`: **NEW ARTIFACT**.
*   `dq-investigation-workflow.yaml`: **NEW ARTIFACT**.
*   `skills/analyze-data-quality-metrics/SKILL.md`: **NEW ARTIFACT**. (Domain skill).
*   `tools/query_data_warehouse.yaml`: **NEW ARTIFACT**. (Infrastructure Gap).

## 7. Skill vs Reference Decisions
The new `analyze-data-quality-metrics` should be a **Skill**. It dictates the procedural steps to take when a DQ alert fires (e.g., check table bounds, check nulls). If specific data warehouse semantics are needed (e.g., "How Snowflake calculates Kurtosis"), that belongs in a `reference/` file within that skill.

## 8. Tool/MCP Analysis
The agent needs to query data to investigate DQ issues.
*   *Needed:* A tool to execute read-only SQL queries against the Data Warehouse.
*   *Existing:* None.
*   *Action:* Create `tools/execute_sql_query.yaml`. Create a new MCP server config (e.g., `snowflake-mcp`) in `mcp/dq-mcp-config.json`.
*   *Security:* The policy MUST enforce `READ` action only. The corporate gateway reference prevents exposing credentials.

## 9. Workflow Analysis
Cannot reuse `replication-investigation-workflow`.
A new `data-quality-investigation-workflow.yaml` is needed.
*   Step 1: Parse table name and DQ metric from alert.
*   Step 2: Query historical data profile (using new SQL tool).
*   Step 3: Analyze deviations (using new DQ Skill).
*   Step 4: Report Findings.

## 10. Evaluation Analysis
A new `data-quality-incident-eval.yaml` is required.
*   *Scenario:* A mock payload showing a sudden spike in NULL values in a Bronze table.
*   *Expected Behavior:* Agent queries the table, applies `analyze-data-quality-metrics`, and correctly infers an upstream schema drift without hallucinating.

## 11. Unknowns / Missing Information
*   What specific Data Warehouse (Snowflake, BigQuery, Databricks SQL) does the DQ agent need to query? (Required to build the correct MCP server).
*   Are there existing DQ frameworks (e.g., Great Expectations, Monte Carlo) that the agent needs to integrate with via MCP?

## 12. Autonomy Test
**Could I implement this correctly using only existing info?**
**YES.** The repository perfectly outlines the architecture. The `README.md`, `AGENTS.md`, and `rules/platform-engineering/artifact-evolution-and-reuse.md` give me the exact 14-step playbook. The distinction between Skill and Reference is clear. The only missing pieces are external domain requirements (which DW to connect to), which I have correctly identified as an UNKNOWN that I would ask the human developer.

## 13. Self-Assessment

| Capability | Score | Justification |
| :--- | :--- | :--- |
| Discoverability | 5 | Directory structure is highly semantic and predictable. |
| Architecture clarity | 5 | `docs/architecture/` leaves no room for confusion regarding Phase 3 vs Phase 4. |
| Agent clarity | 5 | YAML frontmatter clearly binds workflows, skills, and tools. |
| Workflow clarity | 5 | YAML steps are explicit and easy to trace. |
| Skill clarity | 5 | The `SKILL.md` clearly acts as the procedural verb. |
| Reference clarity | 5 | The `reference/` nested structure prevents skill bloat effectively. |
| Baseline vs Domain sep. | 5 | Clearly separated conceptually and structurally. |
| Tool/MCP clarity | 5 | Declarative YAML/JSON makes integration boundaries obvious. |
| Policy/Security clarity | 5 | `policies/` YAML files are explicit and deterministic. |
| Evaluation clarity | 4 | *Minor issue:* `evaluations/replication-incident-eval.yaml` references an obsolete skill (`analyze-kafka-lag`) that was pruned, slightly confusing the dependency graph. |
| Ability to create a new Agent | 5 | The 14-step process makes this foolproof. |
| Overall usability by AI | 5 | Extremely high. The Repo acts as a giant, structured system prompt. |

## 14. Final Verdict
The repository is a resounding success as an Agent Engineering Platform Factory. It achieves true harness independence. A fresh AI agent can read the file structure, understand the ECC-inspired philosophy of declarative artifacts, distinguish between procedural Skills and technical References, and confidently design new Domain Agents (like Data Quality) without writing a single line of Python framework code.
