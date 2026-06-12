from integrations.postgres.db import get_db

def get_logs(service_name: str, limit: int = 100):
    """
    Fetches recent logs for a given service directly from the Prisma Incidents table.
    """
    try:
        db = get_db()
        # Query the Incidents table for recent logs related to this service
        incidents = db.incidents.find_many(
            where={
                "serviceName": service_name,
                "rawLogs": {"not": None}
            },
            order={"createdAt": "desc"},
            take=limit
        )

        logs = []
        for inc in incidents:
            if inc.rawLogs:
                logs.append(inc.rawLogs)

        return logs
    except Exception as e:
        print(f"Error fetching logs from DB: {e}")
        return []