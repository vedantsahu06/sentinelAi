from prisma import Prisma

db = Prisma()

def get_db():
    if not db.is_connected():
        try:
            db.connect()
        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise
    return db