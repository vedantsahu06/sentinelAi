from agent_system.state.sentinel_state import SentinelState

def human_feedback(state: SentinelState) -> dict:
    """
    Simulates receiving human feedback and final resolution data.
    """
    print("---HUMAN FEEDBACK---")

    # In a real system, execution might pause here to wait for user input
    # via a LangGraph interrupt. We simulate it for the hackathon.

    # We pretend the user accepted the first recommendation.
    recs = state.get("recommendations", [])
    accepted_fix = recs[0] if recs else {"description": "Manual intervention", "type": "fix"}

    feedback = {
        "accepted": True,
        "comments": "Fix looks good, deployed to production."
    }

    final_resolution = {
        "applied_fix": accepted_fix,
        "outcome": "Successful",
        "verified": True
    }

    return {"human_feedback": feedback, "final_resolution": final_resolution}
