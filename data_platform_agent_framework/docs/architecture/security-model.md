# Security Model

1. **Authorization is Deterministic:** The Policy Engine dictates access. The LLM cannot grant itself permissions.
2. **Tool Risk:** Every tool has a defined operation type (READ/WRITE) and Risk level.
3. **Human Approval:** High-risk actions require out-of-band human approval (MVP defaults to read-only).
4. **No Secrets in Code:** Secrets must be injected via environment variables or secret managers (mocked in MVP).
