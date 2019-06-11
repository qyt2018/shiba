from utils.model import Model


class AppModel(Model):
    '''
    schema:
        id
        name
        project
        git_uri
        git_user
        git_passwd
        jenkins_job
    '''
    __coll__ = "app"
