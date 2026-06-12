from agent_system.state.sentinel_state import SentinelState

def historical_incident_analysis(state: SentinelState) -> dict:
    """
    Analyzes retrieved memories against the current incident.
    """
    print("---HISTORICAL INCIDENT ANALYSIS---")

    retrieved_memories = state.get("retrieved_memories", [])

    # In a real implementation, an LLM might verify how relevant the memories truly are.
    # Here, we'll just mock filtering for successful resolutions.
    similar_incidents = [
        mem for mem in retrieved_memories
        if mem.get("outcome", "").lower() == "successful"
    ]

    return {"similar_incidents": similar_incidents}
