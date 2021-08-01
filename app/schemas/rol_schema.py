from marshmallow import Schema, fields


class RolSchema(Schema):
    id = fields.Int(dump_only=True)
    rol = fields.Str(required=True)

rol_schema = RolSchema()