from utils.view import View
from services.user import UserService
from forms.user import LoginForm, UserForm
from results.user import UserDetailResult
from utils.auth import login_required, admin_required
from exceptions.model import ModelUniqueException
import logging

logger = logging.getLogger(__name__)


class UserLoginView(View):
    service = UserService
    form = LoginForm

    async def post(self, request):
        form = self.form(data=request.json)
        if form.validate():
            service = self.service()
            is_authenticated, token = await service.authentication(form.username.data, form.password.data)
            if is_authenticated:
                return self.success(f"{token}")
            return self.unauthentication("登录失败，请检查账号密码")
        return self.fail(form.errors)


class UserLogoutView(View):
    decorators = [login_required("user")]
    service = UserService

    async def post(self, request, user):
        service = self.service()
        await service.logout(user)
        return self.success("成功")


class CurrentUserView(View):
    result = UserDetailResult
    decorators = [login_required("user")]

    async def get(self, request, user):
        result = self.result()
        return self.success(result.dump(user).data)


class UserListView(View):
    service = UserService
    result = UserDetailResult
    decorators = [admin_required(), login_required("user")]

    async def get(self, request, user):
        service = self.service()
        result = self.result()
        users = await service.find_users({})
        return self.success(result.dump(users, many=True).data)


class CreateUserView(View):
    service = UserService
    form = UserForm
    result = UserDetailResult
    decorators = [admin_required(), login_required("user")]

    async def post(self, request, user):
        form = self.form(data=request.json)
        if form.validate():
            service = self.service()
            try:
                new_user = await service.create_user(form)
                return self.success(new_user)
            except ModelUniqueException as e:
                logging.error(f"ModelUniqueException: 用户名必须唯一,{e}")
                return self.fail("用户名必须唯一")
        return self.fail(form.errors)
