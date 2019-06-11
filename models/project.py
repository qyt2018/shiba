from utils.model import Model


class ProjectModel(Model):
    '''
    schema:
        id
        name
        owner
        jira_project
        external_links: {
          name
          url
        }
        users: {
          user
          role_key
        }
    '''
    __coll__ = "project"
