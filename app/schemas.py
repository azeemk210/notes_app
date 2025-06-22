from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class NoteIn(BaseModel):
    title: str = Field(..., description="Title of the note")
    content: str = Field(..., description="Content of the note")
    

class NoteOut(NoteIn):
    id: int = Field(..., description="Unique identifier of the note")
    status: str = Field("active", description="Status of the note (e.g., active, archived)")
    created_at: datetime = Field(..., description="Timestamp for when the note was created")
    updated_at: datetime = Field(..., description="Timestamp for when the note was last updated")

class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, description="Title of the note")
    content: Optional[str] = Field(None, description="Content of the note")
    status: Optional[str] = Field(None, description="Status of the note (e.g., active, archived)")
    
class UserCreate(BaseModel):
    username: str = Field(..., description="Username of the user")
    email: str = Field(..., description="Email of the user")
    password: str = Field(..., description="Password of the user")

class UserLogin(BaseModel):
    username: str = Field(..., description="Username of the user")
    password: str = Field(..., description="Password of the user")


class UserOut(BaseModel):
    id: int = Field(..., description="Unique identifier of the user")
    username: str = Field(..., description="Username of the user")
    email: str = Field(..., description="Email of the user")




