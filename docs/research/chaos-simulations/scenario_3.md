# Scenario 3: Cascading Databricks failure via IAM drop
A Databricks pipeline starts throwing `AccessDeniedException` when writing to Silver tables. The actual cause is that the underlying Cloud IAM Service Principal expired. The data pipeline code is flawless, the cluster is healthy, but the external identity provider is the root cause.
