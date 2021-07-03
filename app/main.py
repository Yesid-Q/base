from flask import Flask


def create_app(config):
    app: Flask = Flask(__name__)

    app.config.from_object(config())

    return app 
