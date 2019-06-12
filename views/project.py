from utils import view
from services.user import UserService
from services.project import ProjectService
from forms.project import ProjectDetailForm
from results.project import ProjectDetailResult
from sanic.log import logger
from exceptions.model import ModelUniqueException


class ProjectListView(view.View):
    service = ProjectService
    detail_result = ProjectDetailResult
    search_fields = ('name', 'key')

    async def get(self, request):
        result = self.detail_result()
        service = self.service()
        search_filters = self.get_serach(request)
        page_projects = await service.find_all_project(request, filter=search_filters)
        objects = result.dump(page_projects['objects'], many=True).data
        page_count = page_projects.get('page_count')
        return self.success({"objects": objects, "page_count": page_count})


class ProjectCreateView(view.View):
    service = ProjectService
    user_service = UserService
    detail_form = ProjectDetailForm

    async def post(self, request):
        form = self.detail_form(data=request.json)
        if form.validate():
            service = self.service()
            user_service = self.user_service()
            owner = await user_service.user_exsit_by_id(form.owner.data)
            if not owner:
                return self.fail("负责人不存在")
            try:
                result = await service.create_project(form.data)
                return self.success(result)
            except ModelUniqueException as e:
                logger.error(f"ModelUniqueException: 关键词必须唯一,{e}")
                return self.fail("关键词必须唯一")
        return self.fail(form.errors)
