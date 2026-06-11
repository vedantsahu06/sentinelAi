from agent_system.state.sentinel_state import SentinelState
from tools.database.indexes import check_indexes
from tools.database.slow_queries import get_slow_queries
from tools.monitoring.logs import get_logs

def add_data_to_state(state: SentinelState):

    # Fetch logs
    logs = get_logs()
    # state["logs"] = logs

    # Fetch slow queries
    slow_queries = get_slow_queries()
    # state["slow_queries"] = slow_queries

    # Fetch index analysis
    index_analysis = check_indexes()
    # state["index_analysis"] = index_analysis

    return {
        "logs": logs,
        "slow_queries": slow_queries,
        "index_analysis": index_analysis
    }

