
from peewee import AutoField, CharField, TextField
from app.models import BaseModel

class DocumentModel(BaseModel):
    id = AutoField()
    name = CharField()
    description = TextField()

    class Meta:
        table_name = 'documents'


DocumentModel.create_table()