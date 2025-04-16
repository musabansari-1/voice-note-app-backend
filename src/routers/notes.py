from fastapi import APIRouter, HTTPException
from src.services import notes

router = APIRouter()

@router.get("/notes")
async def get_notes():
    return await notes.get_all_notes()

@router.post("/notes")
async def create_note(title: str, content: str):
    return await notes.create_note(title, content)
