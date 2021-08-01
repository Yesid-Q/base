# importaciones instaladas o de terceros
from flask import Blueprint, request
from peewee import IntegrityError
from marshmallow.exceptions import ValidationError
# importaciones propias
from app.models.user_model import UserModel
from app.models.rol_model import RolModel
from app.schemas.user_schema import user_schema

UserRouter = Blueprint('user', __name__, url_prefix='/user')

@UserRouter.route('/create', methods=['POST'])
def create_user():
    rol = request.args.get('rol', default=1)
    j = request.get_json()
    try:
        schema = user_schema.load(j)
    except ValidationError as err:
        return {"errors": err.messages}, 422
    try:
        user = UserModel.create(rol_id=rol, **schema)
    except IntegrityError as err:
        return {"errors": f'{err}'}, 422

    user = UserModel.select(UserModel, RolModel).join(RolModel).where(UserModel.email == user.email).get()

    return user_schema.dump(user), 201
