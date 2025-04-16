from src.db import get_connection

def get_all_notes():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM notes")
            return cursor.fetchall()
    finally:
        conn.close()

def create_note(title: str, content: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO notes (title, content) VALUES (%s, %s)",
                (title, content)
            )
            conn.commit()
            return {"message": "Note created successfully"}
    finally:
        conn.close()
