from marshmallow import Schema, fields, pre_load


class PlanSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.String(default=None)
    price = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    update_at = fields.DateTime(dump_only=True)
    delete_at = fields.DateTime(dump_only=True)

    @pre_load
    def set_data(cls, data, **kwargs):
        data['title'] = data['title'].lower().strip()
        data['description'] = data['description'].lower().strip() if data['description'] is not None else None
        return data




plan_squema = PlanSchema()
plans_squema = PlanSchema(many=True)