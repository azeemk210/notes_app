from fastapi import APIRouter, Depends, HTTPException
from app.models import Note
from app.schemas import NoteIn, NoteOut, NoteUpdate
from typing import List

router = APIRouter(prefix="/api/notes", tags=["notes"]) 


@router.get("/", response_model=List[NoteOut])
async def get_notes():
    return await Note.all()

@router.get("/{note_id}", response_model=NoteOut)
async def get_note(note_id: int):
    note = await Note.get_or_none(id=note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post("/", response_model=NoteOut)
async def create_note(note_in: NoteIn):
    note = await Note.create(**note_in.dict())
    return note

@router.put("/{note_id}", response_model=NoteOut)
async def update_note(note_id: int, note_in: NoteUpdate):
    note = await Note.get_or_none(id=note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_data = note_in.dict(exclude_unset=True)
    if note_data:
        await note.update_from_dict(note_data).save()
    return note



@router.delete("/{note_id}", response_model=NoteOut)
async def delete_note(note_id: int):
    note = await Note.get_or_none(id=note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    await note.delete()
    return note