from sanic import views
from sanic.response import json


class View(views.HTTPMethodView):
    search_fields = None
    filter_fields = None

    def success(self, data):
        return json({"msg": "成功", "code": 200, "result": data})

    def fail(self, data):
        return json({"msg": "失败", "code": 500, "result": data})

    def unauthentication(self, data):
        return json({"msg": "认证失败", "code": 401, "result": data})

    def get_filter(self, request):
        pass

    def get_serach(self, request):
        if request.raw_args.get('search'):
            filters = []
            for field in self.search_fields:
                filters.append({field: {"$regex": request.raw_args.get('search'), '$options': 'i'}})
            return {"$or": filters}
        else:
            return {}
