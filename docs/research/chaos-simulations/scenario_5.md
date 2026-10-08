# Scenario 5: Multi-tenant throttling
A specific tenant's Kafka partition begins lagging massively. The application code is identical across all tenants. The issue is a "noisy neighbor" on the same physical Databricks cluster exhausting CPU credits, causing the consumer for the specific tenant to be starved of compute, even though the Databricks UI shows the cluster is "Healthy".
