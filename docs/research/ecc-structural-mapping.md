# ECC Structural Mapping

This document maps the actual artifacts found in the ECC repository to their Data Platform Agent Engineering equivalents.

## ECC Repository Metadata
* **Official URL:** https://github.com/affaan-m/everything-claude-code
* **Commit SHA:** ef648e01899ba3e8dc6371642deaaf64b4477775
* **Branch:** main (v2.2.3-1-gef648e01)
* **Inspection Date:** $(date -I)
* **Clone Location:** `/tmp/ecc-reference`
* **Repository Verification:** Complete clone (4,212 tracked files, not shallow).

## Structural Mapping Table

| ECC Artifact | Actual Path(s) | Actual Representation | Purpose | Runtime/Consumer | Data Platform Equivalent | Adopt / Adapt / Reject |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Agent** | `agents/python-reviewer.md`, `agents/planner.md` | Markdown | Defines agent identity, focus, and capabilities. | Loaded into LLM context by runtime script. | **Agent Definition** (Markdown + YAML frontmatter) | **Adapt** (We will use Markdown/YAML for agent definitions, separating them from the Python runtime) |
| **Skill** | `skills/agent-architecture-audit/SKILL.md` | Markdown | Reusable procedural knowledge and domain instructions. | Injected into agent context upon request or relevance. | **Skill** (Markdown) | **Adopt** (Keep as explicit markdown documents describing how to do things) |
| **Workflow** | `workflows/orch-review.workflow.js` | JavaScript | Orchestrates multi-agent/multi-step sequences and rules. | Executed by the Node.js runtime. | **Workflow** (YAML or Python scripts, strictly bounded) | **Adapt** (Represent declarative pipelines as YAML; complex multi-agent execution as strictly controlled Python scripts) |
| **Hook** | `hooks/hooks.json` | JSON | Intercepts tool use to enforce policies (e.g., pre-bash execution). | Intercepted deterministically by the runtime. | **Policy / Hook** (JSON/YAML) | **Adapt** (Represent as explicit JSON/YAML policies enforced by our deterministic Python Policy Engine) |
| **Command** | `commands/epic-claim.md` | Markdown (w/ YAML) | Maps user intents to deterministic execution paths. | Parsed by runtime to execute CLI scripts. | **Tool / Command Definition** (YAML) | **Adapt** (Represent tool schemas/commands explicitly as YAML, executed by Python handlers) |
| **Rule** | `rules/python/testing.md` | Markdown (w/ YAML) | Engineering standards and conventions for specific file scopes. | Injected context based on file path matches. | **Rule** (Markdown) | **Adopt** (Keep as Markdown for LLM consumption during development/review tasks) |
| **MCP Config** | `mcp-configs/mcp-servers.json` | JSON | Defines MCP server launch commands and credentials. | Parsed by runtime to spawn MCP clients. | **MCP Configuration** (JSON) | **Adopt** (Keep as explicit configuration to govern connection/trust parameters) |
| **Runtime** | `scripts/ecc.js`, `scripts/lib/` | JavaScript (Node.js) | Loads artifacts, handles CLI, orchestrates tools, handles state. | Direct execution by user / CI. | **Platform Runtime** (Python) | **Reject/Adapt** (We will implement the runtime in Python, but explicitly separate it from the artifacts as ECC does with JS) |

## Key Formatting Decisions for Data Platform Platform

1. **Agents:** Markdown files with YAML frontmatter. The Markdown contains the system prompt and persona; the YAML defines tools, skills, and allowed MCP servers.
2. **Skills:** Markdown files. Strictly for transferring domain procedural knowledge to the LLM.
3. **Rules:** Markdown files with YAML frontmatter specifying application scopes.
4. **Workflows:** YAML files for declarative step-by-step logic.
5. **Policies:** JSON/YAML files defining deterministic access controls (evaluated by the Python engine, not the LLM).
6. **MCP/Tools:** JSON or YAML configurations defining the schema, decoupled from the Python execution logic.
7. **Runtime Implementation:** Python (but strictly limited to loading the above artifacts, enforcing policies, and executing tools deterministically).
