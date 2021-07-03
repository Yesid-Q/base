from config.settings import Config
from peewee import MySQLDatabase, Model, PostgresqlDatabase

setting = Config()

if setting.DATABASE_DRIVER == 'mysql':
    database = MySQLDatabase(setting.DB_DATABASE, user=setting.USER_DATABASE, password=setting.DATABASE_PASS, host=setting.DATABASE_HOST, port=setting.DATABASE_PORT)
else:
    database = PostgresqlDatabase(setting.DB_DATABASE, user=setting.USER_DATABASE, password=setting.DATABASE_PASS, host=setting.DATABASE_HOST, port=setting.DATABASE_PORT)


class BaseModel(Model):
    class Meta:
        database = database

