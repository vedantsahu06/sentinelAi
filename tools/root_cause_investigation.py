from typing import List, Dict, Any

def root_cause_investigation(parsed_logs: List[Dict], historical_context: List[Dict[str, Any]]) -> str:
    """
    Analyzes logs and historical context to determine a likely root cause.
    """
    # In a full implementation, this might call an LLM directly to analyze
    # the failure chains and historical context.

    # Simple heuristic-based mock
    if historical_context:
        # Heavily weigh historical context if it exists
        return f"Likely related to past issue: {historical_context[0].get('root_cause', 'Unknown')}"

    # Basic log analysis fallback
    for log in parsed_logs:
        message = log.get("message", "").lower()
        if "timeout" in message:
            return "Timeout error in underlying dependency"
        if "oom" in message or "out of memory" in message:
            return "Memory leak in application process"

    return "Unknown Root Cause - requires deeper investigation"
