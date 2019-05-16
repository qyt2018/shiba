from sanic_motor import BaseModel


class ProjectModel(BaseModel):
    __coll__ = "projects"
