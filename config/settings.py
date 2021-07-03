import environ

env = environ.Env()
environ.Env.read_env()

class Config(object):
    SECRET_KEY = env.str('SECRET_KEY')
    DEBUG = env.bool('DEBUG')
    ENV = env.str('ENV')
    DATABASE_DRIVER = env.str('DATABASE_DRIVER')
    USER_DATABASE = env.str('DATABASE_USER')
    DATABASE_PASS = env.str('DATABASE_PASS')
    DATABASE_HOST = env.str('DATABASE_HOST')
    DATABASE_PORT = env.int('DATABASE_PORT')
    DB_DATABASE = env.str('DATABASE_DB')
    