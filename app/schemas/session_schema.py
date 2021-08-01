from marshmallow import Schema, fields, validate

class SessionSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True,validate=[validate.Length(min=6, max=36)])

session_schema = SessionSchema()