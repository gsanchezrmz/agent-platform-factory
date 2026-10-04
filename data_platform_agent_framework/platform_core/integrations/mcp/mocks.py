from typing import Dict, Any

class MockMCPClient:
    def __init__(self):
        self.mock_data = {
            "check_replication_status": {
                "config_123": {"status": "HEALTHY", "lag_seconds": 5},
                "config_456": {"status": "STOPPED", "lag_seconds": 3600}
            },
            "check_bronze_pipeline": {
                "topic_A": {"status": "RUNNING", "last_run": "2024-05-30T10:00:00Z"},
                "topic_B": {"status": "FAILED", "last_run": "2024-05-30T09:00:00Z"}
            }
        }

    def execute_tool(self, tool_identity: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        if tool_identity == "check_replication_status":
            return self.mock_data["check_replication_status"].get(inputs.get("config_id"), {"status": "UNKNOWN", "lag_seconds": -1})
        elif tool_identity == "check_bronze_pipeline":
            return self.mock_data["check_bronze_pipeline"].get(inputs.get("topic"), {"status": "UNKNOWN", "last_run": ""})
        elif tool_identity == "restart_bronze_pipeline":
            return {"result": "Pipeline restart initiated successfully."}
        elif tool_identity == "run_dq_check":
            return {"null_count": 0}
        raise ValueError(f"Unknown tool: {tool_identity}")
