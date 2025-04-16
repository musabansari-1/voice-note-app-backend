from src.db.connection import get_connection

# Fetch all notes
async def get_all_notes():
    conn = await get_connection()
    try:
        rows = await conn.fetch("SELECT * FROM notes")
        return [dict(row) for row in rows]
    finally:
        await conn.close()

# Create a new note
async def create_note(title: str, content: str):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO notes (title, content) VALUES ($1, $2)",
            title, content
        )
        return {"message": "Note created successfully"}
    finally:
        await conn.close()
