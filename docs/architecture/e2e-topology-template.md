# End-to-End Topology Specification (Template)

This template serves as the persistent, declarative source of truth for an environment's End-to-End infrastructure. Any AI Agent operating within this platform must read the populated instance of this document before designing, building, or modifying Domain Agents, Skills, or Tools.

---

## 1. System Overview & Boundaries
* **Environment / Tenant ID:** [e.g., e2e-2627 / Enterprise Production]
* **Primary Mission:** [e.g., Cross-region replication from on-premise transactional systems to cloud lakehouse]
* **Security & Access Boundaries:** [e.g., Strict Read-Only, Corporate API Gateway only, no direct DB write access]

---

## 2. Infrastructure Scale & Topology Dimensions
* **Geographic / Cloud Regions:** [e.g., North America, EMEA, APAC - dynamic expansion possible]
* **Workspaces / Tenants:** [e.g., 1+ Databricks workspaces per region, isolated tenant scopes]
* **Network & Ingress/Egress Constraints:** [e.g., Private VPC peering, outbound egress firewall, VPN tunnels]

---

## 3. Component Anatomy Matrix (Hop-by-Hop)

Every component or node in the end-to-end pipeline must be evaluated across the three fundamental dimensions: **Data State**, **Configuration State**, and **Telemetry/Failure State**.

| Hop # | Component Name | Technology & Hosting | Plane (Control vs Data) | State (Data / Payload) | Configuration (Source & Misconfiguration Risks) | Telemetry & Anomalies (Deceptive / Zombie States) |
|---|---|---|---|---|---|---|
| **01** | [e.g., Source DB] | [e.g., SQL Server 2019 On-Prem] | Data Plane | [e.g., Relational tables, CDC streams] | [e.g., Local DB configs, connection pools, schema drift] | [e.g., SQL Error logs, transaction log full, lock escalation] |
| **02** | [e.g., Replication Config DB] | [e.g., SQL Server Control DB] | Control Plane | [e.g., Metadata tables defining active tables, rates, targets] | [e.g., Control DB tables; risk: inactive flag set, bad rate mapping] | [e.g., Query logs; risk: config cached in memory and not refreshed] |
| **03** | [e.g., Scheduler / Extractor] | [e.g., Windows Service / Hangfire] | Data Plane | [e.g., Polled batch payloads] | [e.g., Local XML/JSON configs, registry keys, appsettings] | [e.g., Service status 'Running' but process deadlocked/hung (Zombie state); requires raw log parsing] |
| **04** | [e.g., Ingestion / Transport] | [e.g., Apache NiFi & Kafka Cluster] | Data Plane | [e.g., Kafka topics, schema registry] | [e.g., Topic retention, partition count, backpressure thresholds] | [e.g., Consumer lag, queue saturation, uncommitted offsets] |
| **05** | [e.g., Lakehouse Ingestion] | [e.g., Databricks Notebooks / Delta Lake] | Data Plane | [e.g., Append to Azure Storage Delta Raw zone] | [e.g., Cluster runtime policies, spark configs, trigger intervals] | [e.g., Driver OOM, stream stalled, permission denied on ADLS] |
| **06** | [e.g., Curated Pipeline] | [e.g., Databricks Delta Live Tables] | Data Plane | [e.g., Raw -> Bronze / Silver / Gold transformations] | [e.g., DLT pipeline settings, expectation thresholds] | [e.g., Expectation failure dropping rows, cluster autoscale delays] |

---

## 4. Known Failure Modes & Deceptive States
List systemic edge cases that naive agents would miss if they only perform surface-level checks:
1. **Deceptive / Zombie Processes:** A service reporting `ACTIVE` or `RUNNING` at the OS level while its internal worker threads are frozen or deadlocked. *Investigation mandate: Always verify unstructured log heartbeats.*
2. **Control Plane vs. Data Plane Drift:** Data pipelines failing silently not because of data corruption, but because a centralized configuration table was updated, disabled, or purged without updating the consumers.
3. **Cross-Region Latency & Quotas:** Network saturation or egress throttling causing upstream backpressure in queues.

---

## 5. Architectural Standards & Tooling Directives
* **Data Access Patterns:** [Direct query, MCP Server via Gateway, REST telemetry endpoints]
* **Log Formats:** [Structured JSON, Unstructured Windows Event/File logs, Datadog/Splunk aggregations]
* **Testing / Mock Strategy:** [Required mock MCP servers to simulate cross-component failure modes]
