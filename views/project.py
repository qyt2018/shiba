from utils import view
from services.user import UserService
from services.project import ProjectService
from forms.project import ProjectDetailForm
from sanic.log import logger
from exceptions.model import ModelUniqueException
from utils.auth import login_required


class ProjectListView(view.View):
    service = ProjectService
    search_fields = ('name', 'key')
    decorators = [login_required("user")]

    async def get(self, request, user):
        service = self.service()
        # 筛选条件
        filter = {"$or": [{'delete': False}, {'delete': None}]}
        search_filters = self.get_serach(request)
        if request.raw_args.get('me') == "true":
            filter['owner'] = str(user.id)
        filter.update(search_filters)

        result = await service.find_all_project(request, filter=filter)
        return self.success(result)


class ProjectDetailView(view.View):
    service = ProjectService
    decorators = [login_required("user")]

    async def get(self, request, user, id):
        service = self.service()
        state, result = await service.get_project(id)
        if state:
            return self.success(result)
        return self.fail(result)


class ProjectCreateView(view.View):
    service = ProjectService
    user_service = UserService
    detail_form = ProjectDetailForm

    async def post(self, request):
        form = self.detail_form(data=request.json)
        if form.validate():
            service = self.service()
            user_service = self.user_service()
            owner = await user_service.user_by_id(form.owner.data)
            if not owner:
                return self.fail("负责人不存在")
            try:
                result = await service.create_project(form.data)
                return self.success(result)
            except ModelUniqueException as e:
                logger.error(f"ModelUniqueException: 关键词必须唯一,{e}")
                return self.fail("关键词必须唯一")
        return self.fail(form.errors)


class ProjectDeleteView(view.View):
    service = ProjectService

    async def post(self, request, id):
        service = self.service()
        state, result = await service.delete_project(id)
        if state:
            return self.success(result)
        return self.fail(result)


class ProjectUpdateView(view.View):
    service = ProjectService
    user_service = UserService
    detail_form = ProjectDetailForm

    async def post(self, request, id):
        form = self.detail_form(data=request.json)
        if form.validate():
            service = self.service()
            user_service = self.user_service()
            owner = await user_service.user_by_id(form.owner.data)
            if not owner:
                return self.fail("负责人不存在")
            try:
                state, result = await service.update_project(id, form.data)
                if state:
                    return self.success(result)
                return self.fail(result)
            except ModelUniqueException as e:
                logger.error(f"ModelUniqueException: 关键词必须唯一,{e}")
                return self.fail("关键词必须唯一")
        return self.fail(form.errors)
