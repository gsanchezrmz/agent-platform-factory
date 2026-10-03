# Dependency Rules

1. **Core -> Nothing:** The `core` module must not depend on `domain` or `agents`.
2. **Domain -> Core:** The `domain` models may depend on `core` abstractions (e.g., Tool definitions).
3. **Integrations -> Core/Domain:** Tools implement `core` MCP abstractions and use `domain` models.
4. **Agents -> Core/Domain/Integrations:** Agents orchestrate components from all other layers.
5. **Security/Policy -> Core:** The Policy Engine sits alongside or within Core to intercept actions. It cannot depend on specific agent implementations.
