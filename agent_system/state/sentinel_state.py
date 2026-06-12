from typing import TypedDict

class SentinelState(TypedDict):
    incident: dict

    logs: list
    slow_queries: list
    index_analysis: dict

    root_cause: str
    confidence: float

    fix: dict