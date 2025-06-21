from fastapi import APIRouter, HTTPException
from app.models import Note, User
from app.schemas import NoteIn, NoteOut, NoteUpdate, UserCreate, UserLogin
from typing import List
from app.security import hash_password, verify_password

router = APIRouter(prefix="/api/notes", tags=["notes"]) 

@router.post("/register")
async def register_user(user_in: UserCreate):
    existing_user = await User.get_or_none(username=user_in.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = hash_password(user_in.password)
    user = await User.create(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password
    )
    return {"message": "User registered successfully", "user_id": user.id}

@router.post("/login")
async def login_user(user_in: UserLogin):
    user = await User.get_or_none(username=user_in.username)
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    return {"message": "Login successful", "user_id": user.id}

@router.get("/users/{user_id}/notes", response_model=List[NoteOut])
async def get_user_notes(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    notes = await Note.filter(user=user).all()
    return notes

@router.get("/users/{user_id}/notes/{note_id}", response_model=NoteOut)
async def get_user_note(user_id: int, note_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    note = await Note.get_or_none(id=note_id, user=user)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    return note

@router.post("/users/{user_id}/notes", response_model=NoteOut)
async def create_user_note(user_id: int, note_in: NoteIn):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    note = await Note.create(**note_in.model_dump(), user=user)
    return note

@router.put("/users/{user_id}/notes/{note_id}", response_model=NoteOut)
async def update_user_note(user_id: int, note_id: int, note_in: NoteUpdate):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    note = await Note.get_or_none(id=note_id, user=user)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    note_data = note_in.model_dump(exclude_unset=True)
    if note_data:
        await note.update_from_dict(note_data).save()
    return note

@router.delete("/users/{user_id}/notes/{note_id}", response_model=NoteOut)
async def delete_user_note(user_id: int, note_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    note = await Note.get_or_none(id=note_id, user=user)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    await note.delete()
    return note
