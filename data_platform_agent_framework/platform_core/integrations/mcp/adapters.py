from dataclasses import dataclass
from typing import Dict, Any
from platform_core.core.tool import Tool, OperationType, RiskLevel

# These act as definitions for our FastMCP tools
def get_replication_status_tool() -> Tool:
    return Tool(
        identity="check_replication_status",
        description="Checks the health of replication for a given config ID.",
        input_schema={"type": "object", "properties": {"config_id": {"type": "string"}}},
        output_schema={"type": "object", "properties": {"status": {"type": "string"}, "lag_seconds": {"type": "integer"}}},
        operation_type=OperationType.READ,
        risk=RiskLevel.LOW,
        environment="PROD" # Can be run in prod safely as it's READ
    )

def get_bronze_pipeline_status_tool() -> Tool:
    return Tool(
        identity="check_bronze_pipeline",
        description="Checks the status of the Databricks Bronze pipeline for a topic.",
        input_schema={"type": "object", "properties": {"topic": {"type": "string"}}},
        output_schema={"type": "object", "properties": {"status": {"type": "string"}, "last_run": {"type": "string"}}},
        operation_type=OperationType.READ,
        risk=RiskLevel.LOW,
        environment="PROD"
    )

def get_restart_pipeline_tool() -> Tool:
    return Tool(
        identity="restart_bronze_pipeline",
        description="Restarts a stopped pipeline.",
        input_schema={"type": "object", "properties": {"pipeline_id": {"type": "string"}}},
        output_schema={"type": "object", "properties": {"result": {"type": "string"}}},
        operation_type=OperationType.EXECUTE,
        risk=RiskLevel.HIGH, # Requires human approval in PROD
        environment="PROD"
    )
