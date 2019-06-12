from .project import ProjectListView, ProjectCreateView
from .user import UserLoginView, UserListView, CreateUserView, CurrentUserView, UserLogoutView, DeleteUserView
from .index import IndexView

urlpatterns = [
    ('/api/user/', UserListView.as_view()),
    ('/api/user/current/', CurrentUserView.as_view()),
    ('/api/user/create/', CreateUserView.as_view()),
    ('/api/user/<user_id>/delete/', DeleteUserView.as_view()),
    ('/api/login/', UserLoginView.as_view()),
    ('/api/logout/', UserLogoutView.as_view()),
    ('/api/project/create', ProjectCreateView.as_view()),
    ('/api/project/', ProjectListView.as_view()),
    ('/<path:path>', IndexView.as_view()),
    ('/', IndexView.as_view())
]
