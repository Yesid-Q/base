# importaciones instaladas o de terceros
from marshmallow import Schema, fields, validate, pre_load

class UserSchema(Schema):
    id = fields.Int(dump_only=True) # dump_only solo sirve para responder, no requiere enviarlo en el json
    username = fields.Str(required=True,validate=[validate.Length(min=6, max=36)]) 
    email = fields.Str(required=True, validate=validate.Email(error="Not a valid email address"))
    password = fields.Str(required=True, validate=[validate.Length(min=6, max=18)], load_only=True) # load_only solo sirve para recibirlo en el json, no lo responde 
    created_at = fields.DateTime(dump_only=True) # dump_only solo sirve para responder, no requiere enviarlo en el json
    update_at = fields.DateTime(dump_only=True) # dump_only solo sirve para responder, no requiere enviarlo en el json
    delete_at = fields.DateTime(dump_only=True) # dump_only solo sirve para responder, no requiere enviarlo en el json

    @pre_load
    def process_data(self, data, **kwargs):
        # convertimos todo a minuscula
        data["username"] = data["username"].lower().strip()
        data["email"] = data["email"].lower().strip()
        return data


user_schema = UserSchema()
users_schema = UserSchema(many=True)

