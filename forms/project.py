from wtforms import form, fields, validators


class ProjectDetailForm(form.Form):
    name = fields.StringField()
