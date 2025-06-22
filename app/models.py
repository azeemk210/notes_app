from tortoise.fields import IntField, CharField, TextField, ForeignKeyField, DatetimeField
from tortoise.models import Model
from datetime import datetime

class User(Model):
    id = IntField(pk=True)
    username = CharField(max_length=50, unique=True)
    email = CharField(max_length=100, unique=True)
    hashed_password = CharField(max_length=255)  # Store hashed passwords

class Note(Model):
    id = IntField(pk=True)
    title = CharField(max_length=255)
    content = TextField()
    status = CharField(max_length=50, default="active")  # Optional status field
    created_at = DatetimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = DatetimeField(auto_now=True)  # Timestamp for last update
    user = ForeignKeyField("models.User", related_name="notes")
    
   

