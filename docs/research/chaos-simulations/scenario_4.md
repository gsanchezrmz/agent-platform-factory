# Scenario 4: Hangfire 200 OK with empty payload
A Hangfire extraction job runs on schedule and returns a green "SUCCESS" state. However, the source API it was extracting data from silently deployed a breaking schema change. The Hangfire job caught the serialization error, logged it as an "INFO" warning to avoid failing the batch, and extracted 0 rows.
