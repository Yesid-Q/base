from flask import g

from app.main import create_app
from config.settings import Config
from app.models import database

from app.routers.user_router import UserRouter
from app.routers. plan_router import PlanRouter

app = create_app(Config)

app.register_blueprint(UserRouter)
app.register_blueprint(PlanRouter)

@app.before_request
def before_request():
    g.db = database
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


if __name__ == '__main__':
    app.run()