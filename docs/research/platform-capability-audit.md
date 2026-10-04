# Platform Capability Audit

This document audits the Phase 3 Agent Engineering foundation to determine if specific Platform Engineering Skills and Domain capabilities exist, and recommends how they should be incorporated.

**Constraint Adherence:** No Phase 4 code has been written, no MCP implementations have been created, and no existing skills were modified during this audit.

## 7. Baseline Platform Capability Audit Table

| Capability | Already Exists | Artifact | Type | Complete | Gap |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MCP dev behind corporate gateway | No | None | Platform Engineering Skill / Rule | No | Missing guidelines for architecture, auth, secrets, network boundaries. |
| Python development | No | None | Rule / Platform Engineering Skill | No | Missing enterprise Python Data Platform coding practices. |
| C# development | No | None | Rule / Platform Engineering Skill | No | Missing enterprise C# coding practices. |
| SQL development | No | None | Rule / Platform Engineering Skill | No | Missing enterprise SQL/Databricks coding practices. |
| Generic log interpretation | No | None | Domain Skill | No | Missing baseline skill for extracting timestamps, severity, and traces. |
| C# log interpretation | No | None | Technology-Specific Skill | No | Missing C#-specific log semantics. |
| SQL error interpretation | No | None | Technology-Specific Skill | No | Missing SQL error semantics. |
| NiFi log interpretation | No | None | Technology-Specific Skill | No | Missing NiFi log semantics (existing skill only handles telemetry metrics). |
| Databricks log interpretation | No | None | Technology-Specific Skill | No | Missing Databricks cluster/job log semantics. |
| Databricks Pipeline interpretation | No | None | Technology-Specific Skill | No | Missing DLT event log semantics. |
| Kafka log interpretation | No | None | Technology-Specific Skill | No | Missing Kafka broker/consumer log semantics (existing skill only handles lag metrics). |

---

## 1. MCP Development Behind a Corporate Gateway
*   **Why it belongs:** The platform relies heavily on FastMCP for domain integrations. An AI coding agent will inevitably be tasked with building these servers. Without explicit instructions on corporate gateway constraints (TLS, auth, rate limiting), the AI will generate insecure or un-deployable code.
*   **Artifact Type:** **Platform Engineering Skill** combined with a **Rule**.
*   **Generic vs Specific:** Generic to MCP architecture within the enterprise, but highly specific to the corporate network topology.
*   **Consumers:** The AI coding harness (Platform Engineering Layer) when extending the platform.
*   **Baseline/Domain:** Baseline platform.

## 2. Component Development by Programming Language
*   **Why it belongs:** An AI agent needs to know the exact enterprise standards for Python, C#, and SQL when writing Data Platform tools or pipelines. Generic LLM knowledge is insufficient for enterprise observability, secret handling, and repo organization.
*   **Artifact Type:** **Rule** (for enforcing standards via `scope: "**/*.py"`) and **Platform Engineering Skill** (for architectural guidance).
*   **Generic vs Specific:** Technology-specific (separate artifacts for Python, C#, SQL). Composable pattern: A generic `code-standards.md` rule, extended by specific `rules/python-standards.md`, etc.
*   **Consumers:** The AI coding harness when writing implementations.
*   **Baseline/Domain:** Baseline platform, as these govern how all future artifacts and tools are written.

## 4. Determine the Correct Skill Granularity (Log Interpretation)
**Recommendation:** **Option B (One generic log-analysis Skill composed with technology-specific Skills).**
*   **Reasoning:**
    *   *Reusability & Composability:* A generic `interpret-logs.md` skill can define the universal procedure: extracting timestamps, severity, correlation IDs, and separating FACT from INFERENCE. This prevents duplicating this boilerplate across 6 different skills.
    *   *Domain Specificity:* The technology-specific skills (e.g., `interpret-kafka-logs.md`) focus purely on the semantics of that technology (e.g., what a `RebalanceInProgress` error means).
    *   *Discoverability:* The AI can compose these: "Use `interpret-logs` combined with `interpret-nifi-logs` to analyze this payload."

## 5. Relationship to the Platform Factory (Classifications)
*   **MCP Dev behind Gateway:** `PLATFORM ENGINEERING SKILL` / `RULE`. It teaches the AI *how* to build safe infrastructure.
*   **Python/C#/SQL Development:** `RULE`. These are engineering standards applied to code generation.
*   **Generic Log Interpretation:** `DOMAIN SKILL`. It teaches an agent how to process text blobs into structured facts.
*   **Kafka/NiFi/Databricks Log Interpretation:** `TECHNOLOGY-SPECIFIC SKILL`. Deep, reusable domain knowledge invoked conditionally based on the system being analyzed.

## 6. Relationship to the Replication Agent
If these capabilities are added, the Replication Agent's workflows will become much more robust.
Currently, the Replication Agent only checks *telemetry* (Lag, Status). If we add log interpretation skills, the `replication-investigation-workflow.yaml` can be extended. For example, if `databricks_state == FAILED`, the workflow can call a new Tool (`get_databricks_logs`), and then invoke the composed Skills (`interpret-logs` + `interpret-databricks-logs`) to find the exact stack trace causing the failure, turning a generic "Target Processing Failure" into a highly specific, actionable Root Cause.
