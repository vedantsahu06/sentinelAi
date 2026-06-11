from agent_system.graphs.sentinel_graph import graph

result = graph.invoke(
    {
        "incident": {
            "type": "high_latency"
        }
    }
)

print(result)