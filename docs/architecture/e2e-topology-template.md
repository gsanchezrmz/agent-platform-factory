# End-to-End (E2E) Topology Mapping Template

Before proposing any Domain Agent or Tool, Platform Architects MUST document the target architecture using this multi-dimensional topology mapping. This ensures Agents do not naively monitor data streams while ignoring the underlying configuration, failure modes, and shared environments.

## 1. State (Data Plane)
*   **Source:** Where does the data originate?
*   **Transit:** How does the data move? (e.g., Kafka, NiFi queues).
*   **Target:** Where does the data land? (e.g., Databricks Bronze table).
*   **Transformation:** What mutates the data in flight?

## 2. Configuration (Control Plane)
*   **Metadata DB:** What database or system controls *whether* the data should flow? (e.g., SQL Server Replication Config table).
*   **Routing/Topology:** Where are the routing rules defined?

## 3. External Dependencies (IAM, Network, Secrets)
*   **Identity & Access:** What IAM roles, Service Principals, or certificates are required for component-to-component transit?
*   **Secrets Engine:** Where are connection strings pulled from?
*   **DNS/Networking:** Are there private endpoints or VNet gateways involved?

## 4. Shared Infrastructure & Isolation Boundaries
*   **Tenancy:** Is this a single-tenant or multi-tenant architecture?
*   **Noisy Neighbors:** What compute/storage resources are shared? (e.g., shared Databricks cluster, shared Kafka broker CPU).
*   **Limits:** Are there API rate limits or compute credit caps that could throttle performance?

## 5. Telemetry (Failure Modes & Anomalies)
*   **Explicit Errors:** What do hard crashes look like in this stack?
*   **Silent Failures:** What does a "zombie" state look like?
*   **Deceptive Telemetry:** Can the system return an Infra 200 OK while failing Business logic?
*   **Anomalies:** What indicates degradation before failure?
