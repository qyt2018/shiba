from .project import ProjectView

urlpatterns = [
    ('/api/project/', ProjectView.as_view())
]
