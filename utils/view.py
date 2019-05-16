from sanic import views
from sanic.response import json


class View(views.HTTPMethodView):

    def success(self, data):
        return json({"msg": "成功", "code": 200, "result": data})

    def fail(self, data):
        return json({"msg": "失败", "code": 500, "result": data})
