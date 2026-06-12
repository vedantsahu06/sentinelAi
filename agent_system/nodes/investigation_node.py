from agent_system.state.sentinel_state import SentinelState
from integrations.llm.groq_client import structured_llm
from pydantic import BaseModel
from services.memory_service import search_memory

class InvestigationOutput(BaseModel):
    incident_type: str
    root_cause: str
    confidence: float
    evidence: str

def investigation_node(state: SentinelState):
    incident = state.get("incident", {})
    incident_type = incident.get("type", "unknown")
    logs = state.get("logs", [])
    queries = state.get("slow_queries", [])
    indexes = state.get("index_analysis", {})

    try:
        historical_memories = search_memory(incident_type, logs)
    except NotImplementedError as e:
        historical_memories = []
        print(f"Skipping memory search: {e}")

    prompt = f"""
    You are a reliability engineer and highly experienced DevOps engineer.
    Your task is to analyze the provided context to classify the incident, determine the root cause, provide a confidence score (0.0 to 100.0), and list the evidence.

    Incident Initial Info:
    {incident}

    Logs:
    {logs}

    Queries:
    {queries}

    Indexes:
    {indexes}

    Historical Incidents (Hindsight Memory):
    {historical_memories}

    Read the above data and find the root cause of the incident.
    """

    try:
        structured_llm1 = structured_llm.with_structured_output(InvestigationOutput)
        result = structured_llm1.invoke(prompt)

        return {
            "root_cause": result.root_cause,
            "confidence": result.confidence,
            "evidence": result.evidence,
            # We add a new field or just rely on confidence. We update state with incident type.
            "incident": {**incident, "type_classified": result.incident_type}
        }
    except Exception as e:
        print(f"LLM Error in investigation node: {e}")
        return {
             "root_cause": "Unknown Root Cause - LLM invocation failed.",
             "confidence": 0.0,
             "evidence": str(e)
        }
