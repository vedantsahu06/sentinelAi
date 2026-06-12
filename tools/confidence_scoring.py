from typing import List, Dict, Any, Tuple

def calculate_confidence_score(root_cause: str, recommendations: List[Dict[str, Any]], historical_context: List[Dict[str, Any]]) -> Tuple[float, str]:
    """
    Estimates confidence level (0-100) and provides reasoning.
    """
    score = 50.0
    reasoning = []

    if historical_context:
        score += 30.0
        reasoning.append("High similarity to historical incidents found.")
    else:
        score -= 20.0
        reasoning.append("No historical precedent found for this issue.")

    if any(rec.get("confidence") == "high" for rec in recommendations):
        score += 15.0
        reasoning.append("Strong recommendation match based on past successful resolutions.")

    if "unknown" in root_cause.lower():
        score -= 25.0
        reasoning.append("Unable to determine specific root cause.")

    # Clamp score
    final_score = max(0.0, min(100.0, score))
    final_reasoning = " ".join(reasoning)

    return final_score, final_reasoning
