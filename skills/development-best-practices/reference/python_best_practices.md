# Python Development Best Practices

This document provides detailed technical knowledge for developing Python components on the Data Platform.

## 1. Project Organization
*   Use `src/` layout (e.g., `src/platform/`, `src/domain/`).
*   Dependency management: Use `uv` or `poetry` (prefer `pyproject.toml` over `requirements.txt` where possible).

## 2. Coding Conventions & Typing
*   **Mandatory Type Hints:** All function signatures and complex variables must use strict type hints (`typing` module or native collections in Python 3.10+).
*   Use `snake_case` for variables/functions, `PascalCase` for classes.
*   Enforce formatting using `ruff` or `black`.

## 3. Error Handling & Exceptions
*   Use custom exception classes inheriting from a base `DataPlatformError`.
*   Never use `except Exception:` without logging the traceback and re-raising, unless explicitly handling a known fallback.

## 4. Configuration & Secrets
*   Use `pydantic-settings` for strongly typed configuration injection.
*   Secrets must be loaded from environment variables (`os.environ` or `.env` files for local dev) and never logged.

## 5. Logging & Observability
*   Use `structlog` or the standard `logging` library configured for JSON output.
*   Bind contextual data (e.g., `pipeline_id`, `correlation_id`) to the logger early in the request lifecycle.

## 6. Testing
*   **Framework:** Use `pytest`.
*   **Mocking:** Use `unittest.mock` (specifically `patch` and `MagicMock`) to isolate I/O boundaries.
*   Ensure tests are placed in a `tests/` directory mirroring the `src/` hierarchy.

## 7. Async Behavior
*   Only use `asyncio` for I/O-bound workloads (e.g., calling multiple FastMCP servers).
*   Avoid mixing sync and async code (`asyncio.run()`) deeply in the call stack.
