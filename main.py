from agent_system.graphs.sentinel_graph import graph

if __name__ == "__main__":
    result = graph.invoke(
        {
            "incident": {
                "type": "high_latency",
                "service": "user-service",
                "description": "Users are reporting timeouts when trying to load their profiles."
            }
        }
    )

    print("\n\n=== RESULT ===")
    print(result)

    print("\n\n=== SENTINEL AI AUDIT REPORT ===")

    print("\n--- TOOL AUDIT ---")
    print("Tool: tools/monitoring/logs.py (get_logs)")
    print(" - Deterministic logic? Yes (fetching external data is deterministic).")
    print(" - Heuristic logic? No.")
    print(" - AI reasoning? No.")
    print(" - Mocked? Yes. (Currently throws NotImplementedError to prevent fake data).")
    print(" - Production-ready? No. Needs Datadog/Splunk integration.")

    print("\nTool: tools/database/slow_queries.py (get_slow_queries)")
    print(" - Deterministic logic? Yes (SQL queries).")
    print(" - Heuristic logic? No.")
    print(" - AI reasoning? No.")
    print(" - Mocked? Yes. (Currently throws NotImplementedError to prevent fake data).")
    print(" - Production-ready? No. Needs real Postgres connection.")

    print("\nTool: tools/database/indexes.py (check_indexes)")
    print(" - Deterministic logic? Yes (SQL queries).")
    print(" - Heuristic logic? No.")
    print(" - AI reasoning? No.")
    print(" - Mocked? Yes. (Currently throws NotImplementedError to prevent fake data).")
    print(" - Production-ready? No. Needs real Postgres connection.")

    print("\nTool: services/memory_service.py (write_memory / search_memory)")
    print(" - Deterministic logic? search_memory relies on pgvector math (deterministic), write_memory is a standard insert.")
    print(" - Heuristic logic? No.")
    print(" - AI reasoning? No (embeddings generation would be AI, but search is math).")
    print(" - Mocked? Yes. (Currently throws NotImplementedError to prevent fake similarity scores/files).")
    print(" - Production-ready? No. Needs Prisma client, pgvector extension, and valid embeddings model.")

    print("\n--- GENERAL AUDIT ---")
    print("1. Mocked Components Remaining:")
    print("   - External data fetching tools and Memory service (isolated behind NotImplementedError interfaces).")
    print("2. Production-Ready Components:")
    print("   - LangGraph State machine structure.")
    print("   - Node prompt logic leveraging Groq LLM (investigation_node, fix_generator_node).")
    print("   - Graph execution pipeline.")
    print("3. Technical Debt:")
    print("   - Implementing actual API calls in the tools (Datadog API, Postgres connection string).")
    print("   - Instantiating standard Langchain memory savers if checkpointing is desired.")
    print("4. Demo Readiness Score:")
    print("   - 45/100. Core architecture is clean, AI prompts are sound and isolated from fakes, but execution relies entirely on missing third-party services.")