from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
import time
import json

@dataclass
class ExecutionEvent:
    event_type: str
    agent_id: str
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)

class ObservabilityTracker:
    def __init__(self):
        self.events: List[ExecutionEvent] = []

    def record_event(self, event_type: str, agent_id: str, metadata: Dict[str, Any] = None):
        event = ExecutionEvent(
            event_type=event_type,
            agent_id=agent_id,
            metadata=metadata or {}
        )
        self.events.append(event)

    def get_events(self) -> List[ExecutionEvent]:
        return self.events

    def dump_logs(self) -> str:
        return json.dumps([
            {
                "type": e.event_type,
                "agent": e.agent_id,
                "ts": e.timestamp,
                "meta": e.metadata
            } for e in self.events
        ], indent=2)
