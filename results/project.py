from marshmallow import Schema, fields


class ProjectDetailResult(Schema):
    id = fields.Str(attribute="_id")
    name = fields.Str()
    key = fields.Str()
