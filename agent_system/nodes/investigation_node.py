from agent_system.state.sentinel_state import SentinelState
from integrations.llm.groq_client import structured_llm
from pydantic import BaseModel

class InvestigationOutput(BaseModel):
    root_cause: str
    confidence: float
    evidence: str
def investigation_node(state: SentinelState):

    logs = state.get("logs")
    queries = state.get("slow_queries")
    indexes = state.get("index_analysis")

    prompt = f"""
    You are a reliability engineer and highly experienced DevOps engineer.

    Logs:
    {logs}

    Queries:
    {queries}

    Indexes:
    {indexes}

    Read the above data and find the root cause of the incident.

    Return:
    root_cause
    confidence
    evidence
    """
    structured_llm1 = structured_llm.with_structured_output(InvestigationOutput)
    result = structured_llm1.invoke(prompt)

    return {
        "root_cause": result.root_cause,
        "confidence": result.confidence,
        "evidence": result.evidence
    }
