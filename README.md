# Data Platform Agent Engineering Platform Factory

Welcome to the Data Platform Agent Engineering Platform Factory.

This repository is **NOT** a standard Python application. It is a portable, declarative **Agent Engineering foundation**. The artifacts in this repository (Markdown, YAML, JSON) teach AI coding agents (like GitHub Copilot, Cursor, Claude, or Gemini) *how to build, evolve, and operate* Data Platform Agents.

The core philosophy, inspired by Everything Claude Code (ECC), is that the knowledge of *what* an agent does, *how* it reasons, and *what* rules it follows must be completely decoupled from the specific LLM harness or Python execution runtime.

## The Two Layers of the Repository

### 1. Platform Engineering Layer (How to Build Agents)
This layer contains the "Meta-Skills" and "Meta-Rules" intended for the AI coding harness that a developer is using to interact with this repository.
*   **Location:** `rules/platform-engineering/` and `skills/platform/`.
*   **Purpose:** It teaches the AI (e.g., Claude) the strict 14-step process for analyzing requirements, inspecting existing coverage, and deciding whether to REUSE, EXTEND, COMPOSE, or create NEW artifacts. It prevents the AI from blindly generating Python code.

### 2. Domain Agent Layer (The Actual Agents)
This layer contains the actual capabilities of the Data Platform Agents.
*   **Agents (`agents/`)**: The core identity (e.g., Replication Monitoring Agent).
*   **Skills (`skills/`)**: Procedural domain knowledge (e.g., how to analyze Kafka lag).
*   **Workflows (`workflows/`)**: Declarative orchestration logic.
*   **Rules & Policies (`rules/`, `policies/`)**: Domain-specific standards and strict, deterministic security boundaries.
*   **Tools & MCP (`tools/`, `mcp/`)**: Definitions of the actual code capabilities the agent can invoke.

## Harness Independence & Portability
This repository is designed to be **Harness Agnostic**.
Whether you use an OpenAI-based agent, a Claude-based harness, or a custom internal tool, the Agent Engineering Artifacts remain identical. The knowledge of how to investigate a Databricks failure (`skills/`) is stored in standard Markdown. The execution workflows (`workflows/`) are standard YAML.

*Future Phase Note:* The Python Platform Runtime (Phase 4) and any specific Harness Adapters will be implemented as execution mechanisms *around* this portable foundation, without requiring changes to the artifacts themselves.

## How to Evolve the Platform
If you are an AI agent reading this, and a human asks you to add a new capability (e.g., a "Data Quality Agent"):
1.  **Stop and Read:** Read `rules/platform-engineering/artifact-evolution-and-reuse.md`.
2.  **Follow the 14 Steps:** Do not immediately write code. Inspect the existing Domain Agent Layer.
3.  **Propose:** Propose a design mapping out the necessary Markdown and YAML files.
4.  **Wait:** Wait for human approval before generating the artifacts.

## Security & Constraints (MVP)
*   **Read-Only:** The current platform policy strictly enforces READ ONLY operations. No agent can mutate state or restart systems.
*   **Fact vs. Inference:** Agents are governed by `rules/investigation-fact-vs-inference.md`, forcing them to distinguish between raw tool data [FACT] and LLM reasoning [INFERENCE].
