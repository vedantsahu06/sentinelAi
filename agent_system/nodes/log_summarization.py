from agent_system.state.sentinel_state import SentinelState
from tools.log_parser import log_parser

def log_summarization(state: SentinelState) -> dict:
    """
    Parses raw logs using the Log Parser tool.
    """
    print("---LOG SUMMARIZATION---")

    raw_logs = state.get("raw_logs", "")
    parsed_logs = log_parser(raw_logs)

    return {"parsed_logs": parsed_logs}
