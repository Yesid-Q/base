from app.models import BaseModel

from peewee import AutoField, CharField, DateTimeField, DoubleField, TextField, TimestampField


class PlanModel(BaseModel):
    id = AutoField(column_name='id')
    title = CharField(column_name='title', max_length=50)
    description = TextField(column_name='description', null=True)
    price = DoubleField(column_name='price')
    created_at = TimestampField()
    update_at = TimestampField()
    delete_at = DateTimeField(null=True)
    
    class Meta:
        table_name = 'plans'

PlanModel.create_table()