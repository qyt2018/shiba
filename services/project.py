from models.project import ProjectModel


class ProjectService(object):
    model = ProjectModel

    async def find_all_project(self):
        model = self.model()
        projects = await model.find()
        return projects.objects

    async def create_project(self, data):
        model = self.model()
        data = await model.insert_one(data)
        return str(data.inserted_id)
