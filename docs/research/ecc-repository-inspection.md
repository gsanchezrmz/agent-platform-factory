# ECC Repository Inspection

## Repository Metadata
* **Official URL:** https://github.com/affaan-m/everything-claude-code
* **Commit SHA:** ef648e01899ba3e8dc6371642deaaf64b4477775
* **Branch:** main (v2.2.3-1-gef648e01)
* **Inspection Date:** $(date -I)
* **Clone Location:** `/tmp/ecc-reference`
* **Repository Verification:** Complete clone (4,212 tracked files, not shallow).

## Actual Repository Structure
The repository demonstrates a highly organized separation of Agent Engineering concepts, using explicit directories:
* `agents/` - Contains `.md` files defining various specialized agents (e.g., `code-reviewer.md`, `python-reviewer.md`, `planner.md`).
* `skills/` - Contains subdirectories for individual skills (295 total). Each directory typically contains a `SKILL.md` (e.g., `skills/agent-architecture-audit/SKILL.md`).
* `hooks/` - Contains hook configurations, JSON files, and javascript scripts (e.g., `hooks.json`).
* `commands/` - Contains `.md` files documenting specific commands and their implementation scripts/paths (e.g., `epic-claim.md`).
* `rules/` - Contains `.md` files documenting engineering standards/rules categorized by domains (e.g., `rules/python/testing.md`).
* `workflows/` - Contains JavaScript files representing orchestrations of skills/agents (e.g., `orch-review.workflow.js`).
* `mcp-configs/` - Contains `mcp-servers.json` mapping MCP capabilities to CLI commands/servers.
* `scripts/` - Contains the runtime implementation in Node.js/JavaScript, including `ecc.js`, `install-apply.js`, `dashboard-web.js`, etc.

## Representative Artifacts

### 1. Agent
* **Example:** `agents/python-reviewer.md`
* **Format:** Markdown
* **Purpose:** Defines the identity, instructions, and focus areas for a specialized python reviewing agent.
* **How it is used:** Loaded as a context/system prompt for an LLM session dynamically.

### 2. Skill
* **Example:** `skills/agent-architecture-audit/SKILL.md`
* **Format:** Markdown
* **Purpose:** Provides a comprehensive definition of a capability (auditing agent architecture), including instructions, procedures, and expected outcomes.
* **How it is used:** Included as context or referenced by agents and workflows to grant them specific procedural knowledge.

### 3. Hook
* **Example:** `hooks/hooks.json`
* **Format:** JSON (wrapping JavaScript/Bash commands)
* **Purpose:** Defines intercepts for tools/actions (e.g., `PreToolUse` for `Bash` or `Write`), executing specific node scripts (`scripts/hooks/gateguard-fact-force.js`) before allowing the LLM action.
* **How it is used:** Executed deterministically by the runtime/framework intercepting LLM tool calls.

### 4. Command
* **Example:** `commands/epic-claim.md`
* **Format:** Markdown (with YAML frontmatter)
* **Purpose:** Maps a conceptual slash command (e.g., `/epic-claim`) to a specific executable script (`scripts/github-coordination.js claim ...`).
* **How it is used:** Read by the platform to route user intents/commands to underlying deterministic execution.

### 5. Rule
* **Example:** `rules/python/testing.md`
* **Format:** Markdown (with YAML frontmatter specifying file paths)
* **Purpose:** Defines coding standards (e.g., use `pytest`, `pytest.mark` for categorization) applied to specific file globs.
* **How it is used:** Injected into context when specific files/paths are being modified or reviewed to enforce standards.

### 6. MCP Configuration
* **Example:** `mcp-configs/mcp-servers.json`
* **Format:** JSON
* **Purpose:** Defines the available MCP servers (e.g., `nexus`, `jira`, `github`), their execution commands, arguments, and required environment variables.
* **How it is used:** Loaded by the runtime to establish MCP client connections and expose tools to the LLM.

## Important Finding
**Is ECC primarily organized as a Python framework, or as a collection of reusable Agent Engineering artifacts supported by runtime/configuration?**

Based on repository evidence, ECC is strictly **a collection of reusable Agent Engineering artifacts (Markdown, JSON) supported by a JavaScript (Node.js) runtime.**
There are no monolithic `Agent` or `Skill` classes in the codebase. The runtime (`scripts/`) exists completely separated from the definitions of the agents (`agents/`), the skills they use (`skills/`), and the rules they follow (`rules/`). The platform deterministically parses these declarative and descriptive files to orchestrate interactions.
