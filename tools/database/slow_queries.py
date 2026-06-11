def get_slow_queries():
    return [
        {
            "query": "SELECT * FROM users WHERE email=?",
            "avg_time_ms": 2400
        }
    ]