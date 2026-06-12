import re
from typing import List, Dict

def log_parser(raw_logs: str) -> List[Dict]:
    """
    Parses raw text logs into structured dictionaries.
    Assumes standard format e.g., '[TIMESTAMP] [LEVEL] [SERVICE] MESSAGE'.
    """
    structured_logs = []
    # Basic regex pattern for generic log lines
    pattern = re.compile(r'\[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)')

    for line in raw_logs.strip().split('\n'):
        match = pattern.match(line)
        if match:
            structured_logs.append({
                "timestamp": match.group(1).strip(),
                "level": match.group(2).strip(),
                "service": match.group(3).strip(),
                "message": match.group(4).strip(),
            })
        else:
            # Fallback for unparseable lines
            structured_logs.append({
                "raw_line": line.strip()
            })

    return structured_logs
