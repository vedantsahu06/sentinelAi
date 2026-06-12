from typing import List, Dict

def incident_classifier(parsed_logs: List[Dict]) -> str:
    """
    Classifies incident data based on keywords in the structured logs.
    Categories: database, authentication, network, memory, cpu, deployment, security, dependency, unknown
    """
    categories = {
        "database": ["database", "db", "sql", "connection pool", "timeout"],
        "authentication": ["auth", "login", "unauthorized", "forbidden", "401", "403"],
        "network": ["network", "tcp", "refused", "timeout", "latency"],
        "memory": ["memory", "oom", "out of memory", "leak"],
        "cpu": ["cpu", "load", "spike", "throttling"],
        "deployment": ["deploy", "release", "pod", "container"],
        "security": ["security", "breach", "exploit", "vulnerability"],
        "dependency": ["dependency", "package", "npm", "pip", "version"],
    }

    # Simple keyword matching approach
    for log in parsed_logs:
        message = log.get("message", "").lower()
        if not message:
            message = log.get("raw_line", "").lower()

        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in message:
                    return category

    return "unknown"
