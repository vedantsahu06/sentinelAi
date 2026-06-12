from agent_system.state.sentinel_state import SentinelState
from tools.incident_classifier import incident_classifier

def incident_classification(state: SentinelState) -> dict:
    """
    Classifies the incident based on parsed logs using the Incident Classifier tool.
    """
    print("---INCIDENT CLASSIFICATION---")

    parsed_logs = state.get("parsed_logs", [])
    incident_type = incident_classifier(parsed_logs)

    return {"incident_type": incident_type}
