# Replication Investigation Skill
**Knowledge:** Replication pulls data from on-prem DBs to Kafka/Databricks.
**Procedures:** If replication is STOPPED, you must check the downstream Bronze pipeline status.
**Heuristics:** A FAILED downstream pipeline is the most common cause of STOPPED upstream replication.
