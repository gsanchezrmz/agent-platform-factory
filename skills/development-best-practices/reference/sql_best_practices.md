# SQL Development Best Practices

This document provides detailed technical knowledge for developing SQL queries, views, and migrations on the Data Platform.

## 1. Query Structure & Readability
*   Use Common Table Expressions (CTEs - `WITH` clauses) instead of deeply nested subqueries to improve readability and debugging.
*   Format queries with capitalized keywords (`SELECT`, `FROM`, `JOIN`) and consistent indentation.
*   Use explicit aliases for all tables (e.g., `FROM users u`).

## 2. Joins & Filtering
*   Always use explicit joins (`INNER JOIN`, `LEFT JOIN`) rather than comma-separated `FROM` clauses.
*   Filter data as early as possible (in the `ON` clause or initial CTE) to reduce intermediate result set sizes.

## 3. NULL Handling
*   Be explicit when handling NULLs. Use `COALESCE()` or `IFNULL()` (vendor dependent) instead of relying on implicit behavior.
*   Remember that `NOT IN (SELECT column_with_nulls)` will return no results if a NULL is present. Use `NOT EXISTS` instead.

## 4. Performance & Indexes
*   Avoid `SELECT *` in production code; explicitly name required columns.
*   Avoid functions on indexed columns in `WHERE` clauses (e.g., `WHERE YEAR(created_at) = 2023`), as this prevents index seeks (non-sargable).
*   Ensure foreign keys and frequently filtered columns have appropriate indexes.

## 5. Security & Injection
*   **Mandatory Parameterization:** Never concatenate strings to build SQL queries in application code. Always use parameterized queries or ORMs to prevent SQL injection.

## 6. Concurrency & Transactions
*   Wrap multi-step write operations in explicit transactions (`BEGIN TRAN` / `COMMIT`).
*   Keep transactions as short as possible to prevent locking/blocking issues.
*   Understand the default isolation level of your target database (e.g., Read Committed vs. Snapshot).

## 7. Migrations & Schema Changes
*   All schema changes must be idempotent and managed via version-controlled migration scripts (e.g., Flyway, Liquibase, EF Core Migrations).
*   Never drop a column or table in a single deployment if it is actively queried by production code (use a multi-phase deprecation strategy).
