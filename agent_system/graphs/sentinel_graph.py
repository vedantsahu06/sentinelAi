from agent_system.state.sentinel_state import SentinelState
from langgraph.graph import START, StateGraph,END
from agent_system.nodes.investigation_node import investigation_node
from agent_system.nodes.fix_generator_node import fix_generator_node
from agent_system.nodes.add_data_to_state import add_data_to_state
workflow = StateGraph(SentinelState)

workflow.add_node("investigation", investigation_node)
workflow.add_node("fix_generator", fix_generator_node)
workflow.add_node("add_data", add_data_to_state)
workflow.add_edge(START, "add_data")
workflow.add_edge("add_data", "investigation")
workflow.add_edge("investigation", "fix_generator")
workflow.add_edge("fix_generator", END)

graph= workflow.compile()