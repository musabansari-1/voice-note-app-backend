from fastapi import APIRouter, HTTPException
from src.services import notes

router = APIRouter()

@router.get("/notes")
def get_notes():
    return notes.get_all_notes()

@router.post("/notes")
def create_note(title: str, content: str):
    return notes.create_note(title, content)
