from wtforms import form, fields, validators


class ProjectDetailForm(form.Form):
    name = fields.StringField(validators=[validators.DataRequired(message="名称必填")])
    key = fields.StringField(validators=[validators.DataRequired(message="关键词必填"),
                                         validators.Regexp("^[A-Z]+$", message="关键词必须由大写字母组成")])
    owner = fields.StringField(validators=[validators.DataRequired(message="负责人必填")])
