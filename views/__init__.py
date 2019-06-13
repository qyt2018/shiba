from .project import ProjectListView, ProjectCreateView, ProjectDeleteView, ProjectUpdateView, ProjectDetailView, \
    ProjectAddLinkView, ProjectDeleteLinkView
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
    ('/api/project/<id>/delete/', ProjectDeleteView.as_view()),
    ('/api/project/<id>/update/', ProjectUpdateView.as_view()),
    ('/api/project/<id>/add_link/', ProjectAddLinkView.as_view()),
    ('/api/project/<id>/delete_link/', ProjectDeleteLinkView.as_view()),
    ('/api/project/<pk>/', ProjectDetailView.as_view()),
    ('/api/project/', ProjectListView.as_view()),
    ('/<path:path>', IndexView.as_view()),
    ('/', IndexView.as_view())
]
