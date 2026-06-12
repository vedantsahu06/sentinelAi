from typing import TypedDict, Any, List

class SentinelState(TypedDict, total=False):
    incident_id: str
    raw_logs: str
    parsed_logs: List[dict]
    incident_type: str
    severity: str
    service_name: str
    similar_incidents: List[dict]
    retrieved_memories: List[dict]
    root_cause: str
    recommendations: List[dict]
    confidence_score: float
    human_feedback: dict
    final_resolution: dict
    memory_written: bool
