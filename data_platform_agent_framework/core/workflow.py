from dataclasses import dataclass, field
from typing import List, Callable, Any

@dataclass
class WorkflowStep:
    name: str
    action: Callable[..., Any]
    requires_approval: bool = False

@dataclass
class Workflow:
    name: str
    description: str
    steps: List[WorkflowStep] = field(default_factory=list)
