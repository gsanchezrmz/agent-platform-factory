# Skill: Agent Architecture Design

This skill belongs to the **Platform Engineering Layer**. It teaches an AI coding harness how to architect a new Data Platform Agent or evolve existing agent capabilities systematically.

---

## Purpose
To ensure that all proposed agents, skills, and tools conform to the declarative framework, respect environmental topology, and account for distributed configurations and deceptive failure modes without hardcoding assumptions.

---

## Core Architectural Heuristics

### 1. The Component Anatomy Pattern
Every component in the data pipeline (databases, message queues, cloud runtimes, background services) must be decomposed into three investigative dimensions:
* **State (Data):** What data does this hop produce, consume, or transform?
* **Configuration (Control Plane):** Where are the governing settings stored (e.g. control database, config YAML, environment flags, API registry)? How can misconfigurations (rate limits, disabled flags, schema mismatches) break the downstream pipeline?
* **Telemetry & Deceptive Failure Modes:** How can this component fail silently? (e.g., Windows services in a "Running" state while hung, Kafka consumer lag growing with zero error logs, Databricks cluster autoscale stalling).

### 2. Context-First Dependency Analysis
Before proposing any tool or skill:
1. Cross-reference `docs/architecture/` to verify that the target system and access pattern (e.g., Corporate Gateway vs direct connection) are documented.
2. If the component's configuration source is unknown, flag a **CONTEXT GAP** and request clarification from the developer. Do not guess default connection strings or APIs.

### 3. Evaluation & Simulation Mandate
Never design an Agent or Tool without specifying how it will be validated. Every proposal must include:
* Synthetic incident scenario (what failure is simulated?).
* Mock MCP server requirement (what tool outputs are mocked?).
* Verification assertion (how do we prove the agent correctly distinguished FACT from INFERENCE?).

---

## Drafting the Architectural Proposal

When asked to design or evolve an agent, format your proposal with this exact structure:

1. **Environmental Baseline:**
   * Referenced E2E Topology and verified components.
   * Identified Control Planes vs Data Planes.
2. **Reuse & Composition Assessment:**
   * Existing Agents to REUSE or EXTEND.
   * Existing Skills and Workflows to COMPOSE.
3. **Identified Gaps:**
   * **Scope Gap:** What domain knowledge is missing?
   * **Infrastructure Gap:** What declarative tools in `tools/` or servers in `mcp/` are needed?
   * **Context Gap:** What unverified assumptions remain?
4. **Proposed Artifact Changes:**
   * Exact file paths to be created (`.md`, `.yaml`, `.json`).
   * Explicit justification against the 14-step process.
5. **Evaluation Strategy:**
   * Synthetic test scenario to be added to `evaluations/`.
6. **Required Human Clarifications:**
   * Questions on ambiguous infrastructure before execution begins.
