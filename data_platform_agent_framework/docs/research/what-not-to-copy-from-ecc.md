# What Not To Copy From ECC

## Overview
While the ECC (Everything Claude Code) philosophy is inspiring, it is heavily tailored toward software development in a local or highly trusted environment. A Data Platform Engineering Platform requires a different trust model and operational paradigm.

## Concepts Not to Copy

### 1. Arbitrary Code/Command Execution
- **ECC approach:** Can run `npm run build`, `git commit`, `bash` scripts freely to solve problems.
- **Why it doesn't apply:** A Data Platform Agent cannot execute arbitrary commands against production databases, Databricks clusters, or Kafka brokers. All actions must go through strictly defined tools (MCPs) with specific input schemas.

### 2. LLM-Driven Authorization
- **ECC approach:** The LLM often decides what is safe to run based on system prompts.
- **Why it doesn't apply:** We need a deterministic, out-of-band Policy Engine. The LLM must request an action, and the Policy Engine (evaluating identity, tool risk, and environment) decides if it's allowed.

### 3. Broad File System Access
- **ECC approach:** Has full read/write access to the repository to make changes.
- **Why it doesn't apply:** The agent should not be modifying its own source code or unrelated platform files. Access is limited to specific domain data (e.g., replication configs, logs).

### 4. Over-reliance on Complex RAG/Memory for the MVP
- **ECC approach:** May use complex memory structures to remember past coding sessions.
- **Why it doesn't apply:** For our MVP (Replication Monitoring & Investigation), a simple transactional context is sufficient. Complex RAG introduces unnecessary architectural overhead.

### 5. Lack of Domain Boundaries
- **ECC approach:** A general-purpose coding assistant.
- **Why it doesn't apply:** We need a strict separation between the Platform Core (Agent, Policy, Tools) and the Domain (Databases, Replication, Databricks).
