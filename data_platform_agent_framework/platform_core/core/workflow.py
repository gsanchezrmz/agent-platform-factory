from dataclasses import dataclass, field
from typing import List, Callable, Any, Dict
from platform_core.observability.observability import ObservabilityTracker

@dataclass
class WorkflowStep:
    name: str
    # action takes runtime_context (dict) and returns a result
    action: Callable[[Dict[str, Any]], Any]

class Workflow:
    def __init__(self, identity: str, description: str, steps: List[WorkflowStep]):
        self.identity = identity
        self.description = description
        self.steps = steps

    def execute(self, runtime_context: Dict[str, Any], tracker: ObservabilityTracker) -> Any:
        tracker.record_event("WORKFLOW_START", runtime_context.get("agent_id", "unknown"), {"workflow": self.identity})
        last_result = None
        for step in self.steps:
            tracker.record_event("WORKFLOW_STEP", runtime_context.get("agent_id", "unknown"), {"step": step.name})
            try:
                last_result = step.action(runtime_context)
                # Store intermediate results in context
                runtime_context[step.name] = last_result
            except Exception as e:
                tracker.record_event("WORKFLOW_ERROR", runtime_context.get("agent_id", "unknown"), {"step": step.name, "error": str(e)})
                raise
        tracker.record_event("WORKFLOW_COMPLETE", runtime_context.get("agent_id", "unknown"), {"workflow": self.identity})
        return last_result
