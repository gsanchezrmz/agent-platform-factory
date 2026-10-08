# C# & .NET Log Analysis

## Semantics
*   **Exceptions:** Pay attention to the Exception Type (e.g., `NullReferenceException`, `SqlException`, `TaskCanceledException`).
*   **Stack Traces:** The top of the stack trace in C# represents the exact method where the exception was thrown. The bottom represents the entry point (e.g., `Main` or the HTTP controller).
*   **TaskCanceledException / OperationCanceledException:** Usually indicates a timeout (e.g., HttpClient timeout) or that the user aborted the HTTP request.

## Common Patterns
*   `ObjectDisposedException`: A resource (like a database connection) was used after being closed. This is an application logic bug.
*   `InvalidOperationException`: A broad exception indicating the state of the object is incompatible with the requested method (e.g., calling `.First()` on an empty LINQ collection).
