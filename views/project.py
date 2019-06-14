from utils import view
from services.user import UserService
from services.project import ProjectService
from forms.project import ProjectDetailForm, ProjectLinkForm, ProjectUserForm
from sanic.log import logger
from exceptions.model import ModelUniqueException
from utils.auth import login_required
import uuid


class ProjectListView(view.View):
    service = ProjectService
    search_fields = ('name', 'key')
    decorators = [login_required("user")]

    async def get(self, request, user):
        service = self.service()
        # 筛选条件
        search_filters = self.get_serach(request)
        filter = {"$or": [{'delete': False}, {'delete': None}]}
        if request.raw_args.get('me') == "true":
            filter['owner'] = str(user.id)
        filter = {'$and': [filter, search_filters]}
        result = await service.find_all_project(request, filter=filter)
        return self.success(result)


class ProjectDetailView(view.View):
    service = ProjectService
    decorators = [login_required("user")]

    async def get(self, request, user, pk):
        service = self.service()
        state, result = await service.get_project(pk)
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


class ProjectAddLinkView(view.View):
    service = ProjectService
    form = ProjectLinkForm

    async def post(self, request, id):
        form = self.form(data=request.json)
        if form.validate():
            service = self.service()
            data = form.data
            data['id'] = str(uuid.uuid4())
            state, result = await service.project_add_link(id, data)
            if state:
                return self.success(result.get('links', []))
            return self.fail(result)
        return self.fail(form.errors)


class ProjectDeleteLinkView(view.View):
    service = ProjectService

    async def post(self, request, id):
        link_id = request.json.get('link_id')
        if link_id:
            service = self.service()
            state, result = await service.project_delete_link(id, link_id)
            if state:
                return self.success(result.get('links', []))
            return self.fail(result)
        return self.fail("未找到URL")


class ProjectAddUserView(view.View):
    service = ProjectService
    form = ProjectUserForm

    async def post(self, request, id):
        form = self.form(data=request.json)
        if form.validate():
            service = self.service()
            data = form.data
            data['id'] = str(uuid.uuid4())
            has_user = await service.project_has_user(id, form.user.data)
            result = "项目成员已存在"
            if not has_user:
                state, result = await service.project_add_user(id, data)
                if state:
                    return self.success(result)
            return self.fail(result)
        return self.fail(form.errors)


class ProjectdeleteUserView(view.View):
    service = ProjectService

    async def post(self, request, id):
        service = self.service()
        row_id = request.json.get('row_id')
        result = "未找到ID"
        if row_id:
            state, result = await service.project_delete_user(id, row_id)
            if state:
                return self.success(result)
        return self.fail(result)


class ProjectUserView(view.View):
    service = ProjectService

    async def get(self, request, id):
        service = self.service()
        state, result = await service.get_project_user(id)
        if state:
            return self.success(result)
        return self.fail(result)
