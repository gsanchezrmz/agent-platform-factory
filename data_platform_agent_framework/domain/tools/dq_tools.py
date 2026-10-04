from platform_core.core.tool import Tool, OperationType, RiskLevel

def get_dq_check_tool() -> Tool:
    return Tool(
        identity="run_dq_check",
        description="Runs a data quality check on a table.",
        input_schema={"type": "object", "properties": {"table": {"type": "string"}}},
        output_schema={"type": "object", "properties": {"null_count": {"type": "integer"}}},
        operation_type=OperationType.READ,
        risk=RiskLevel.LOW,
        environment="PROD"
    )
