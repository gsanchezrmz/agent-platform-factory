# Agent Guide

This file provides programmatic and contextual instructions for AI Agents (like Claude, Codex, etc.) working within this repository.

## Repository Context
You are working inside the **Data Platform Agent Engineering Platform**.
This is NOT a standard Python application. It is an artifact-driven framework.

## Your Responsibilities
When creating or modifying capabilities within this platform, you MUST respect the architectural boundaries:

1.  **Do not write Python logic to define Agents.** Agents, Skills, Workflows, Rules, and Policies MUST be defined declaratively in their respective folders (`agents/`, `skills/`, `workflows/`, etc.) using Markdown, YAML, or JSON.
2.  **Skills are Markdown.** If you are asked to teach an agent how to do something, you write a `.md` file in `skills/`. You do not write a Python function.
3.  **Python is for Runtime only.** Python code (in `platform/` or `domain/`) is strictly reserved for deterministic execution (loading artifacts, enforcing policies, executing API calls).

## Validation Checks
If you are modifying this repository, perform these checks:
1.  Did I accidentally hardcode domain knowledge (like Kafka lag thresholds) into a Python file? (It belongs in a Skill).
2.  Did I define the tool schema explicitly in `tools/` before trying to use it?
3.  Does my new Agent definition properly reference existing or new Skills?
