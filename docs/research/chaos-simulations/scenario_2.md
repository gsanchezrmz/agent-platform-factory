# Scenario 2: Zombie NiFi processors
A NiFi processor is in a "RUNNING" state according to the API, and there are 0 errors in the logs. However, the internal thread pool is deadlocked. The queue before it is empty because upstream routing stopped, but it should be processing heartbeats. It is silently hung.
