from langgraph.graph import START, StateGraph, END
from agent_system.state.sentinel_state import SentinelState

# Import nodes
from agent_system.nodes.log_ingestion import log_ingestion
from agent_system.nodes.log_summarization import log_summarization
from agent_system.nodes.incident_classification import incident_classification
from agent_system.nodes.memory_retrieval import memory_retrieval
from agent_system.nodes.historical_incident_analysis import historical_incident_analysis
from agent_system.nodes.root_cause_investigation import root_cause_investigation
from agent_system.nodes.recommendation_generation import recommendation_generation
from agent_system.nodes.confidence_scoring import confidence_scoring
from agent_system.nodes.human_feedback import human_feedback
from agent_system.nodes.memory_persistence import memory_persistence

workflow = StateGraph(SentinelState)

# Add nodes
workflow.add_node("log_ingestion", log_ingestion)
workflow.add_node("log_summarization", log_summarization)
workflow.add_node("incident_classification", incident_classification)
workflow.add_node("memory_retrieval", memory_retrieval)
workflow.add_node("historical_incident_analysis", historical_incident_analysis)
workflow.add_node("root_cause_investigation", root_cause_investigation)
workflow.add_node("recommendation_generation", recommendation_generation)
workflow.add_node("confidence_scoring", confidence_scoring)
workflow.add_node("human_feedback", human_feedback)
workflow.add_node("memory_persistence", memory_persistence)

# Add edges (sequential flow)
workflow.add_edge(START, "log_ingestion")
workflow.add_edge("log_ingestion", "log_summarization")
workflow.add_edge("log_summarization", "incident_classification")
workflow.add_edge("incident_classification", "memory_retrieval")
workflow.add_edge("memory_retrieval", "historical_incident_analysis")
workflow.add_edge("historical_incident_analysis", "root_cause_investigation")
workflow.add_edge("root_cause_investigation", "recommendation_generation")
workflow.add_edge("recommendation_generation", "confidence_scoring")
workflow.add_edge("confidence_scoring", "human_feedback")
workflow.add_edge("human_feedback", "memory_persistence")
workflow.add_edge("memory_persistence", END)

graph = workflow.compile()
