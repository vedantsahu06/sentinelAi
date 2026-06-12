from agent_system.state.sentinel_state import SentinelState
from integrations.llm.groq_client import structured_llm
from pydantic import BaseModel
from services.memory_service import write_memory

class FixOutput(BaseModel):
    fix: str
    risk: str
    rollback: str

def fix_generator_node(state: SentinelState):
    root_cause = state.get("root_cause", "")
    confidence = state.get("confidence", 0.0)
    evidence = state.get("evidence", "")

    incident = state.get("incident", {})
    incident_type = incident.get("type", "unknown")
    logs = state.get("logs", [])

    prompt = f"""
    You are a reliability engineer and highly experienced DevOps engineer.
    Generate a fix for this incident.

    Root Cause: {root_cause}
    Evidence: {evidence}
    Confidence in Root Cause: {confidence}/100

    Include:
    - Detailed step by step fix (SQL if applicable)
    - Risk assessment
    - Rollback commands to revert the state if the fix causes issues.

    Return JSON matching the schema.
    """

    try:
        structured_llm1 = structured_llm.with_structured_output(FixOutput)
        result = structured_llm1.invoke(prompt)

        fix_desc = f"Fix: {result.fix}\nRisk: {result.risk}\nRollback: {result.rollback}"

        # Attempt to write to memory
        try:
            write_memory(incident_type, logs, root_cause, fix_desc)
        except NotImplementedError as e:
            print(f"Skipping memory write: {e}")

        return {
            "fix": {"description": fix_desc}
        }
    except Exception as e:
        print(f"LLM Error in fix generator node: {e}")
        return {
            "fix": {"description": "Manual intervention required. LLM generation failed."}
        }
