from utils.model import Model


class TaskModel(Model):
    '''
    schema:
        id
        name
        type
        state
        project
        apps: []
        release_time
        real_release_time
        remark
        jira_version
        create_user
        create_time
    '''
    __coll__ = "task"
