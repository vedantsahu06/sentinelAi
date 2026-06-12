from agent_system.state.sentinel_state import SentinelState
from tools.memory_search import memory_search

def memory_retrieval(state: SentinelState) -> dict:
    """
    Retrieves similar past incidents using the Memory Search tool.
    """
    print("---MEMORY RETRIEVAL---")

    incident_data = {
        "incident_type": state.get("incident_type"),
        "parsed_logs": state.get("parsed_logs")
    }

    retrieved_memories = memory_search(incident_data)

    return {"retrieved_memories": retrieved_memories}
