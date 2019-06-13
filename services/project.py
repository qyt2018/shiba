from models.project import ProjectModel
from services.user import UserService


class ProjectService(object):
    model = ProjectModel

    async def get_project_result(self, project):
        result = {
            'id': str(project.id),
            'name': project.name,
            'key': project.key,
            'owner': None
        }
        user_service = UserService()
        owner = await user_service.user_by_id(project.owner)
        if owner:
            result['owner'] = user_service.get_user_result(owner)
        return result

    async def find_all_project(self, request, filter):
        model = self.model()
        objects = []
        page_objects = await model.page_find(request, filter=filter)
        for project in page_objects['objects']:
            objects.append(await self.get_project_result(project))
        return {'objects': objects,
                'page_count': page_objects['page_count']}

    async def create_project(self, data):
        model = self.model()
        data = await model.insert_one(data)
        return str(data.inserted_id)

    async def delete_project(self, id):
        project = await self.model.find_one(id)
        if project:
            await self.model.update_one({u'_id': project.id}, {'$set': {"delete": True}})
            return True, "删除成功"
        return False, "未找到用户"
