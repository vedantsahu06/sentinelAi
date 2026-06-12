from agent_system.state.sentinel_state import SentinelState

def log_ingestion(state: SentinelState) -> dict:
    """
    Ingests raw logs. In a real system, this might fetch logs based on incident_id.
    """
    print("---LOG INGESTION---")

    # Simulating fetching raw logs
    raw_logs = state.get("raw_logs")
    if not raw_logs:
        raw_logs = "[2023-10-28T12:00:00Z] [ERROR] [auth-service] Connection timeout to database\n[2023-10-28T12:00:05Z] [WARN] [auth-service] Retrying connection"

    return {"raw_logs": raw_logs}
