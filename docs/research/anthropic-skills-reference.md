# Anthropic Skills Reference Inspection

## Repository Metadata
* **Official URL:** https://github.com/anthropics/skills
* **Path Inspected:** `skills/mcp-builder`
* **Inspection Date:** $(date -I)

## Findings on Conceptual Organization

### 1. Skill Structure (The "Verb")
*   **Location:** `SKILL.md` (e.g., `skills/mcp-builder/SKILL.md`)
*   **Metadata:** Uses YAML frontmatter to declare `name` and `description` (including `Use when...` instructions).
*   **Content Focus:** The `SKILL.md` is strictly procedural. It provides the "Process" (Phase 1: Deep Research, Phase 2: Implementation, Phase 3: Testing). It teaches the AI *how* to approach the task (e.g., "Balance API coverage vs workflow tools").
*   **References:** It delegates deep technical specifics by pointing the AI to external reference files.

### 2. Reference Material Structure (The "Noun")
*   **Location:** `reference/` directory (e.g., `reference/mcp_best_practices.md`, `reference/python_mcp_server.md`).
*   **Content Focus:** These files are highly specific, factual, and technical. For instance, `mcp_best_practices.md` explicitly lists naming conventions (`snake_case`, `{service}_{action}_{resource}`), pagination standards (`has_more`, `next_offset`), and transport rules. `python_mcp_server.md` likely provides exact syntax and library usage.
*   **Consumption:** An AI Agent is expected to load `SKILL.md` to understand the workflow, and conditionally load the specific `reference/*.md` files when it actually needs to write the code (e.g., loading `python_mcp_server.md` when tasked with a Python build).

### 3. Key Takeaway for Data Platform Agent Engineering
*   **Strict Separation:** We must mirror this separation. Our `SKILL.md` files will dictate *how* to analyze a log or *how* to develop a component. Our `skills/X/reference/` directories will contain the factual semantics (e.g., C# conventions, Kafka error codes) to prevent the `SKILL.md` from becoming bloated or language-specific.
*   **Declarative Nature:** None of these are executable Python files. They are Markdown artifacts acting as extended, composable system prompts for LLMs.
