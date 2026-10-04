# Agent Guide

This file provides programmatic and contextual instructions for AI Agents (like GitHub Copilot, Claude, Gemini, Codex, etc.) working within this repository.

## Repository Context
You are working inside the **Data Platform Agent Engineering Platform Factory**.
This repository is the source of truth for Agent Engineering knowledge. It is completely decoupled from any specific LLM or Python execution runtime.

## Your Primary Directive
When a human developer asks you to implement a new feature, agent, or capability, **you must read and follow `rules/platform-engineering/artifact-evolution-and-reuse.md`**.

You are expected to act as a Platform Engineer. You must:
1.  Understand the 14-step Agent Engineering Process.
2.  Categorize requested changes as REUSE, EXTEND, COMPOSE, NEW, INFRASTRUCTURE GAP, or EVALUATION GAP.
3.  Propose the architecture using the `skills/platform/agent-architecture-design.md` skill.
4.  **Never write Python code to define an Agent, Skill, or Workflow.** All agent logic belongs in explicit declarative artifacts (`.md`, `.yaml`, `.json`).

## Harness Independence
Do not write logic that assumes the presence of a specific LLM (like GPT-4) or a specific harness (like Copilot). The artifacts you create must be purely declarative and universally parseable.
