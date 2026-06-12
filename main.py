from agent_system.graphs.sentinel_graph import graph

result = graph.invoke(
    {
        "incident_id": "inc-12345",
        "service_name": "user-service",
        "raw_logs": "[2023-10-28T12:00:00Z] [ERROR] [user-service] Connection timeout to database"
    }
)

import pprint
pprint.pprint(result)
