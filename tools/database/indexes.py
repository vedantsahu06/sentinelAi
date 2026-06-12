from integrations.postgres.db import get_db

def check_indexes(table_name: str = None):
    """
    Analyzes database indexes using actual pg_stat_user_indexes.
    """
    try:
        db = get_db()
        # Query pg_stat_user_indexes to find unused indexes or basic index stats
        query = "SELECT relname, indexrelname, idx_scan FROM pg_stat_user_indexes;"
        if table_name:
            query = f"SELECT relname, indexrelname, idx_scan FROM pg_stat_user_indexes WHERE relname = '{table_name}';"

        result = db.query_raw(query)

        # Format the result to match the expected dictionary structure if needed
        formatted_result = {}
        for row in result:
             if isinstance(row, dict):
                  formatted_result[f"{row.get('relname')}.{row.get('indexrelname')}"] = row.get('idx_scan', 0)
        return formatted_result
    except Exception as e:
        print(f"Error fetching indexes from DB: {e}")
        return {}