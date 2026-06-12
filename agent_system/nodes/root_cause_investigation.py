from agent_system.state.sentinel_state import SentinelState
from tools.root_cause_investigation import root_cause_investigation as rca_tool

def root_cause_investigation(state: SentinelState) -> dict:
    """
    Runs the RCA tool to update the root_cause state.
    """
    print("---ROOT CAUSE INVESTIGATION---")

    parsed_logs = state.get("parsed_logs", [])
    similar_incidents = state.get("similar_incidents", [])

    root_cause = rca_tool(parsed_logs, similar_incidents)

    return {"root_cause": root_cause}
