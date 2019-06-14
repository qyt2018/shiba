from wtforms import form, fields, validators
from enums.project import ProjectRoleEnums


class ProjectDetailForm(form.Form):
    name = fields.StringField(validators=[validators.DataRequired(message="名称必填")])
    key = fields.StringField(validators=[validators.DataRequired(message="关键词必填"),
                                         validators.Regexp("^[A-Z]+$", message="关键词必须由大写字母组成")])
    owner = fields.StringField(validators=[validators.DataRequired(message="负责人必填")])


class ProjectLinkForm(form.Form):
    name = fields.StringField(validators=[validators.DataRequired(message="名称必填")])
    url = fields.StringField(validators=[validators.DataRequired(message="关键词必填"),
                                         validators.URL(message="输入正确的URL")])


class ProjectUserForm(form.Form):
    user = fields.StringField(validators=[validators.DataRequired(message="用户必填")])
    role_key = fields.SelectField(validators=[validators.DataRequired(message="角色必填")],
                                  choices=ProjectRoleEnums.choices(), coerce=ProjectRoleEnums.coerce)
