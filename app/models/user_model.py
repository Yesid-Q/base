# importaciones principales
from datetime import datetime
# importaciones instaladas o de terceros
from werkzeug.security import generate_password_hash
from peewee import AutoField, BooleanField, CharField, DateTimeField, ForeignKeyField, TextField, TimestampField
# importaciones propias
from app.models import BaseModel
from app.models.document_model import DocumentModel

class UserModel(BaseModel):
    id = AutoField(column_name='id',)
    username = CharField(column_name='username', unique=True)
    email = CharField(column_name='email', max_length=100, unique=True)
    password = CharField(column_name='password', max_length=150)
    is_admin = BooleanField(default=False)
    remember_token = TextField(null=True)

    document = ForeignKeyField(DocumentModel)
    
    created_at = TimestampField(column_name='created_at')
    update_at = TimestampField(column_name='update_at')
    delete_at = DateTimeField(column_name='delete_at', null=True)

    class Meta:
        table_name = 'users'

    def save(self, *args, **kwargs):
        self.make_password()
        super(UserModel, self).save(*args, **kwargs)

    def make_password(self):
        self.password = generate_password_hash(self.password, method='sha256')

    def delete(self):
        self.delete_at = None if self.delete_at is not None else datetime.now()
        self.save()

    
UserModel.create_table()