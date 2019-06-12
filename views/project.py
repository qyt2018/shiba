from utils import view
from services.user import UserService
from services.project import ProjectService
from forms.project import ProjectDetailForm
from sanic.log import logger
from exceptions.model import ModelUniqueException


class ProjectListView(view.View):
    service = ProjectService
    search_fields = ('name', 'key')

    async def get(self, request):
        service = self.service()
        search_filters = self.get_serach(request)
        result = await service.find_all_project(request, filter=search_filters)
        return self.success(result)


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
