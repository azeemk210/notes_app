from tortoise.fields import IntField, CharField, TextField, ForeignKeyField
from tortoise.models import Model

class User(Model):
    id = IntField(pk=True)
    username = CharField(max_length=50, unique=True)
    email = CharField(max_length=100, unique=True)
    hashed_password = CharField(max_length=255)  # Store hashed passwords

class Note(Model):
    id = IntField(pk=True)
    title = CharField(max_length=255)
    content = TextField()
    user = ForeignKeyField("models.User", related_name="notes")
    

