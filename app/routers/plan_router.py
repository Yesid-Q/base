from flask import Blueprint, request

from marshmallow.exceptions import ValidationError
from peewee import IntegrityError

from app.schemes.plan_schema import plan_squema, plans_squema
from app.models.plan_model import PlanModel

PlanRouter = Blueprint('plan',__name__, url_prefix='/plan')

@PlanRouter.route('/', methods=['GET'])
def list_plan():
    query = PlanModel.select()
    return plans_squema.dumps(query)

@PlanRouter.route('/create/', methods=['POST'])
def create_plan():
    j = request.get_json()

    try:
        schema = plan_squema.load(j)
    except ValidationError as err:
        return {"errors": err.messages}, 422
    try:
        plan = PlanModel.create(**schema)
    except IntegrityError as err:
        return {"errors": f'{err}'}, 422
    return schema