from agent_system.state.sentinel_state import SentinelState
from tools.confidence_scoring import calculate_confidence_score

def confidence_scoring(state: SentinelState) -> dict:
    """
    Computes and updates the confidence_score based on findings.
    """
    print("---CONFIDENCE SCORING---")

    root_cause = state.get("root_cause", "")
    recommendations = state.get("recommendations", [])
    similar_incidents = state.get("similar_incidents", [])

    score, reasoning = calculate_confidence_score(root_cause, recommendations, similar_incidents)

    print(f"Confidence Score: {score} - Reason: {reasoning}")

    return {"confidence_score": score}
