from agent_system.state.sentinel_state import SentinelState
from tools.recommendation import generate_recommendations

def recommendation_generation(state: SentinelState) -> dict:
    """
    Runs the Recommendation tool to generate fixes and verification steps.
    """
    print("---RECOMMENDATION GENERATION---")

    root_cause = state.get("root_cause", "")
    similar_incidents = state.get("similar_incidents", [])

    recommendations = generate_recommendations(root_cause, similar_incidents)

    return {"recommendations": recommendations}
