from flask import abort, Blueprint, jsonify, make_response, request

from marshmallow.exceptions import ValidationError

from app.models.user_model import UserModel
from app.models.rol_model import RolModel
from app.schemas.session_schema import session_schema
from app.schemas.user_schema import user_schema

SessionRouter = Blueprint('session', __name__, url_prefix='/sesion')


@SessionRouter.route('/login', methods=['POST'])
def session_login():
    data = request.get_json()
    try:
        schema = session_schema.load(data)
    except ValidationError as err:
        abort(make_response(jsonify(msg='error', errors= err.messages),422))

    user: UserModel = UserModel.login(email=data['email'], password=data['password'])
    user.create_jwt()
    user = UserModel.select(UserModel, RolModel).join(RolModel).where(UserModel.email == data['email']).get()
    return user_schema.dump(user)