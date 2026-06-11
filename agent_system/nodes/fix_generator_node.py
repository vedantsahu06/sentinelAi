from langgraph.types import interrupt, Command, RetryPolicy
from agent_system.state.sentinel_state import SentinelState
from integrations.llm.groq_client import structured_llm
from pydantic import BaseModel



class FixOutput(BaseModel):
    fix: str

def fix_generator_node(state: SentinelState):
    root_cause = state.get("root_cause")
    confidence = state.get("confidence")
    evidence = state.get("evidence")



    prompt = f"""
    you are a reliability engineer and highly experienced DevOps engineer.
Generate a fix.
for this root cause: {root_cause}
Include:

SQL
Risk
Rollback commands -> such that if the fix causes issues, we can quickly rollback to the previous state.by using this commnand

Return JSON only.

"""
    structured_llm1 = structured_llm.with_structured_output(FixOutput)
    result = structured_llm1.invoke(prompt)

    return {
        "fix": result.fix
    }
