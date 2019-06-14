from models.project import ProjectModel
from services.user import UserService
from enums.project import ProjectRoleEnums
from bson import ObjectId
import uuid


class ProjectService(object):
    model = ProjectModel

    async def get_project_result(self, project):
        result = {
            'id': str(project.id),
            'name': project.name,
            'key': project.key,
            'owner': None,
            'links': []
        }
        user_service = UserService()
        owner = await user_service.user_by_id(project.owner)
        if owner:
            result['owner'] = user_service.get_user_result(owner)
        if project.links:
            for link in project.links:
                result['links'].append({'name': link['name'], 'url': link['url'], 'id': str(link['id'])})
        return result

    async def get_project_user_result(self, project):
        result = []
        user_service = UserService()
        owner = await user_service.user_by_id(project.owner)
        owner_result = {
            'id': str(uuid.uuid4()),
            'role_key': ProjectRoleEnums.OWNER.name,
            'role_name': ProjectRoleEnums.OWNER.value,
            'user': project.owner,
            'user_detail': user_service.get_user_result(owner)
        }
        result.append(owner_result)
        if project.users:
            for user in project.users:
                user_obj = await user_service.user_by_id(user['user'])
                user['user_detail'] = user_service.get_user_result(user_obj)
                result.append(user)
        return result

    async def get_project(self, pk):
        project = await self.model.find_one(pk)
        if not project:
            project = await self.model.find_one({'key': pk})
        if project:
            return True, await self.get_project_result(project)
        return False, "未找到项目"

    async def get_project_user(self, pk):
        project = await self.model.find_one(pk)
        if not project:
            project = await self.model.find_one({'key': pk})
        if project:
            return True, await self.get_project_user_result(project)
        return False, "未找到项目"

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
        return False, "未找到项目"

    async def update_project(self, id, data):
        project = await self.model.find_one(id)
        if project:
            await self.model.update_one({u'_id': project.id}, {'$set': data})
            return True, "更新成功"
        return False, "未找到项目"

    async def project_add_link(self, id, data):
        project = await self.model.find_one(id)
        if not project:
            project = await self.model.find_one({'key': id})
        if project:
            await self.model.update_one({u'_id': project.id}, {'$push': {"links": data}})
            project = await self.get_project(id)
            return True, project[1]
        return False, "未找到项目"

    async def project_delete_link(self, id, link_id):
        project = await self.model.find_one(id)
        if not project:
            project = await self.model.find_one({'key': id})
        if project:
            await self.model.update_one({u'_id': project.id}, {'$pull': {"links": {'id': link_id}}})
            project = await self.get_project(id)
            return True, project[1]
        return False, "未找到项目"

    async def project_add_user(self, id, data):
        project = await self.model.find_one(id)
        if not project:
            project = await self.model.find_one({'key': id})
        if project:
            data['role_name'] = ProjectRoleEnums[data['role_key']].value
            await self.model.update_one({u'_id': project.id}, {'$push': {"users": data}})
            project = await self.get_project_user(id)
            return True, project[1]
        return False, "未找到项目"

    async def project_delete_user(self, id, row_id):
        project = await self.model.find_one(id)
        if not project:
            project = await self.model.find_one({'key': id})
        if project:
            await self.model.update_one({u'_id': project.id}, {'$pull': {"users": {'id': row_id}}})
            project = await self.get_project_user(id)
            return True, project[1]
        return False, "未找到项目"

    async def project_has_user(self, key, user):
        if await self.model.find_one({'key': key, "users": {'$elemMatch': {'user': user}}}):
            return True
        if await self.model.find_one({'key': key, "owner": user}):
            return True
        return False
