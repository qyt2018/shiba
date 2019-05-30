from wtforms import form, fields, validators


class LoginForm(form.Form):
    username = fields.StringField(validators=[validators.DataRequired(message="用户名必填")])
    password = fields.StringField(validators=[validators.DataRequired(message="密码必填")])


class UserForm(form.Form):
    name = fields.StringField(validators=[validators.DataRequired(message="用户名必填")])
    username = fields.StringField(validators=[validators.DataRequired(message="用户名必填")])
    password = fields.StringField(validators=[validators.DataRequired(message="密码必填")])
    is_admin = fields.BooleanField(default=False)
