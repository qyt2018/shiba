from models.project import ProjectModel


class ProjectService(object):
    model = ProjectModel

    async def find_all_project(self, request, filter):
        model = self.model()
        page_objects = await model.page_find(request, filter=filter)
        return page_objects

    async def create_project(self, data):
        model = self.model()
        data = await model.insert_one(data)
        return str(data.inserted_id)
