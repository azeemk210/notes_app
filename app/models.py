from tortoise.fields import IntField, CharField, TextField
from tortoise.models import Model

class Note(Model):
    id = IntField(pk=True)
    title = CharField(max_length=255)
    content = TextField()

    

