from marshmallow import Schema, fields


class UserDetailResult(Schema):
    id = fields.Str(attribute="_id")
    name = fields.Str()
    username = fields.Str()
    is_admin = fields.Bool()
    scope = fields.Method("get_scope")

    def get_scope(self, obj):
        if obj.is_admin:
            return ["admin", "user"]
        return ["user"]
