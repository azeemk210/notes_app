from pydantic import BaseModel, Field
from typing import Optional, List

class NoteIn(BaseModel):
    title: str = Field(..., description="Title of the note")
    content: str = Field(..., description="Content of the note")

class NoteOut(NoteIn):
    id: int = Field(..., description="Unique identifier of the note")

class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, description="Title of the note")
    content: Optional[str] = Field(None, description="Content of the note")