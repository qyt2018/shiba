from utils import view
from services.project import ProjectService
from forms.project import ProjectDetailForm
from results.project import ProjectDetailResult


class ProjectView(view.View):
    service = ProjectService
    detail_form = ProjectDetailForm
    detail_result = ProjectDetailResult

    async def get(self, request):
        result = self.detail_result()
        service = self.service()
        projects = await service.find_all_project()
        data = result.dump(projects, many=True)
        return self.success(data)

    async def post(self, request):
        service = self.service()
        form = self.detail_form(data=request.data)
        if form.validate():
            result = await service.create_project(form.data)
            return self.success(result)
        return self.fail("创建失败")
