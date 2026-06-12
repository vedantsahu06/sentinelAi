from typing import List, Dict, Any
from integrations.postgres.db import get_db
from sentence_transformers import SentenceTransformer

# Initialize the embedding model (downloads it locally if not present)
model = SentenceTransformer('all-MiniLM-L6-v2')

def _generate_embedding(text: str) -> List[float]:
    """
    Generates a 384-dimensional embedding using SentenceTransformers.
    """
    embedding = model.encode(text)
    return embedding.tolist()

def write_memory(incident_id: str, incident_type: str, logs: List[Any], root_cause: str, final_resolution: str) -> bool:
    """
    Stores incident knowledge to Hindsight memory via Prisma using real semantic vectors.
    """
    try:
        db = get_db()
        search_text = f"{incident_type} {str(logs)} {root_cause} {final_resolution}"
        embedding = _generate_embedding(search_text)

        # Verify incident exists, else insert it first so foreign key constraints pass
        incident = db.incidents.find_unique(where={"id": incident_id})
        if not incident:
             db.incidents.create(data={
                 "id": incident_id,
                 "type": incident_type,
                 "serviceName": "unknown",
                 "rawLogs": str(logs)
             })

        # Insert using raw SQL because Prisma schema defines embedding as Unsupported("vector")
        db.query_raw(
            '''
            INSERT INTO "IncidentMemories" ("id", "incidentId", "rootCause", "resolution", "outcome", "timestamp", "embedding")
            VALUES (gen_random_uuid(), $1, $2, $3, $4, NOW(), $5::vector)
            ''',
            incident_id, root_cause, final_resolution, "Successful", str(embedding)
        )
        return True
    except Exception as e:
        print(f"Error writing memory to DB: {e}")
        return False

def search_memory(incident_type: str, logs: List[Any]) -> List[Dict[str, Any]]:
    """
    Searches Hindsight memory and computes a semantic similarity score via pgvector/Prisma
    using real embeddings.
    """
    try:
        db = get_db()
        search_text = f"{incident_type} {str(logs)}"
        embedding = _generate_embedding(search_text)

        # Search using pgvector cosine distance operator <=>
        results = db.query_raw(
            '''
            SELECT
                "rootCause" as root_cause,
                "resolution",
                "outcome",
                1 - ("embedding" <=> $1::vector) as similarity_score
            FROM "IncidentMemories"
            ORDER BY similarity_score DESC
            LIMIT 5
            ''',
            str(embedding)
        )

        formatted_results = []
        for row in results:
             if isinstance(row, dict):
                  formatted_results.append({
                      "root_cause": row.get("root_cause"),
                      "resolution": row.get("resolution"),
                      "outcome": row.get("outcome"),
                      "similarity_score": row.get("similarity_score")
                  })
        return formatted_results
    except Exception as e:
        print(f"Error searching memory in DB: {e}")
        return []