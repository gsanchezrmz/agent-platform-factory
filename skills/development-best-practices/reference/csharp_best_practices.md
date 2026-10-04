# C# Development Best Practices

This document provides detailed technical knowledge for developing C# / .NET components on the Data Platform.

## 1. Project Organization & Namespaces
*   Organize solutions by domain (e.g., `DataPlatform.Replication.Api`, `DataPlatform.Replication.Tests`).
*   Namespaces must strictly match the directory structure.

## 2. Coding Conventions & Types
*   **Nullability:** Enable `<Nullable>enable</Nullable>` in all `.csproj` files. Treat nullable warnings as errors.
*   Use `PascalCase` for public members/classes, `camelCase` for locals, and `_camelCase` for private fields.
*   Prefer `record` types for immutable Data Transfer Objects (DTOs).

## 3. Dependency Injection & Interfaces
*   Rely on `Microsoft.Extensions.DependencyInjection`.
*   Inject interfaces (`IReplicationService`), not concrete implementations, to enable testability.
*   Register services with the correct lifetime (`AddTransient`, `AddScoped`, `AddSingleton`) to prevent captive dependencies.

## 4. Async/Await & Concurrency
*   **Mandatory Async:** Use `async/await` for all I/O operations (Database, HTTP).
*   **Cancellation:** Pass `CancellationToken` through all asynchronous call stacks.
*   Avoid `Task.Run` for I/O bounds; avoid `.Result` or `.Wait()` to prevent deadlocks (sync-over-async anti-pattern).

## 5. Configuration & Secrets
*   Use the Options Pattern (`IOptions<T>`, `IOptionsSnapshot<T>`) for strongly typed configuration.
*   Use Azure Key Vault, AWS Secrets Manager, or User Secrets (local) for sensitive data. Never hardcode credentials in `appsettings.json`.

## 6. Logging & Observability
*   Use structured logging via `ILogger<T>`.
*   Log templates must use semantic names, not string interpolation (e.g., `_logger.LogInformation("Processing pipeline {PipelineId}", id);`).
*   Propagate `System.Diagnostics.Activity` for distributed tracing.

## 7. Resource Management
*   Implement `IDisposable` or `IAsyncDisposable` for classes holding unmanaged resources or long-lived connections.
*   Use `using` declarations to ensure deterministic disposal.
*   When using `HttpClient`, use `IHttpClientFactory` to prevent socket exhaustion; do not instantiate `HttpClient` manually in loops.

## 8. Testing & Validation
*   **Frameworks:** Use `xUnit` for test execution, `Moq` or `NSubstitute` for mocking dependencies, and `FluentAssertions` for readability.
*   Validate inputs at the API boundary using `FluentValidation` or DataAnnotations.
