from agent_system.state.sentinel_state import SentinelState
from tools.memory_writer import memory_writer

def memory_persistence(state: SentinelState) -> dict:
    """
    Calls the Memory Writer tool to persist the incident knowledge.
    """
    print("---MEMORY PERSISTENCE---")

    incident_data = {
        "id": state.get("incident_id"),
        "type": state.get("incident_type"),
        "service": state.get("service_name")
    }
    root_cause = state.get("root_cause", "")
    final_resolution = state.get("final_resolution", {})

    success = memory_writer(incident_data, root_cause, final_resolution)

    return {"memory_written": success}
