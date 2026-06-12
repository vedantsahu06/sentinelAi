from integrations.postgres.db import get_db

def get_slow_queries(limit: int = 5):
    """
    Fetches the slowest recent queries from the database using pg_stat_statements.
    """
    try:
        db = get_db()
        # Query pg_stat_statements for actual slow queries
        query = f"SELECT query, mean_exec_time as avg_time_ms FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT {limit};"
        result = db.query_raw(query)
        return result
    except Exception as e:
        print(f"Error fetching slow queries from DB: {e}")
        return []