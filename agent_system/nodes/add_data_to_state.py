from agent_system.state.sentinel_state import SentinelState
from tools.database.indexes import check_indexes
from tools.database.slow_queries import get_slow_queries
from tools.monitoring.logs import get_logs

def add_data_to_state(state: SentinelState):
    incident_info = state.get("incident", {})
    service_name = incident_info.get("service", "unknown-service")

    # Fetch logs
    try:
        logs = get_logs(service_name)
    except NotImplementedError as e:
        logs = []
        print(f"Skipping logs: {e}")

    # Fetch slow queries
    try:
        slow_queries = get_slow_queries()
    except NotImplementedError as e:
        slow_queries = []
        print(f"Skipping slow queries: {e}")

    # Fetch index analysis
    try:
        index_analysis = check_indexes()
    except NotImplementedError as e:
        index_analysis = {}
        print(f"Skipping index analysis: {e}")

    return {
        "logs": logs,
        "slow_queries": slow_queries,
        "index_analysis": index_analysis
    }
