from .project import ProjectView
from .user import UserLoginView, UserListView

urlpatterns = [
    ('/api/user/', UserListView.as_view()),
    ('/api/login/', UserLoginView.as_view()),
    ('/api/project/', ProjectView.as_view())
]
