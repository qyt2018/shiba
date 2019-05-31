from .project import ProjectView
from .user import UserLoginView, UserListView, CreateUserView, CurrentUserView, UserLogoutView, DeleteUserView

urlpatterns = [
    ('/api/user/', UserListView.as_view()),
    ('/api/user/current/', CurrentUserView.as_view()),
    ('/api/user/create/', CreateUserView.as_view()),
    ('/api/user/<user_id>/delete/', DeleteUserView.as_view()),
    ('/api/login/', UserLoginView.as_view()),
    ('/api/logout/', UserLogoutView.as_view()),
    ('/api/project/', ProjectView.as_view())
]
