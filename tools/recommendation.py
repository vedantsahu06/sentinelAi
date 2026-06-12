from typing import List, Dict, Any

def generate_recommendations(root_cause: str, historical_context: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Generates fixes, investigation steps, rollback suggestions, and verification steps based on RCA.
    """
    recommendations = []

    # Check if historical context has a proven resolution
    if historical_context:
        past_resolution = historical_context[0].get("resolution")
        if past_resolution:
            recommendations.append({
                "type": "fix",
                "description": f"Apply historically successful fix: {past_resolution}",
                "confidence": "high"
            })

    # Add general fallback recommendations based on root cause string
    rc_lower = root_cause.lower()

    if "memory" in rc_lower:
        recommendations.append({
            "type": "investigation",
            "description": "Capture a heap dump and restart the service to clear memory.",
            "confidence": "medium"
        })
    elif "connection" in rc_lower or "timeout" in rc_lower:
        recommendations.append({
            "type": "fix",
            "description": "Increase connection pool size or timeout thresholds in configuration.",
            "confidence": "medium"
        })
    else:
         recommendations.append({
            "type": "investigation",
            "description": "Review recent deployments for potential breaking changes.",
            "confidence": "low"
        })

    return recommendations
