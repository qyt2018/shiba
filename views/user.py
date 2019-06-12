from utils.view import View
from services.user import UserService
from forms.user import LoginForm, UserForm
from utils.auth import login_required, admin_required
from exceptions.model import ModelUniqueException
from sanic.log import logger


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
            logger.info(token)
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
    decorators = [login_required("user")]

    async def get(self, request, user):
        result = {
            "id": str(user.id),
            "name": user.name,
            "username": user.username,
            "is_admin": user.is_admin,
            "scope": ["user"]
        }
        if user.is_admin:
            result['scope'].append("admin")
        return self.success(result)


class UserListView(View):
    service = UserService
    decorators = [admin_required(), login_required("user")]

    async def get(self, request, user):
        service = self.service()
        result = await service.find_users({})
        return self.success(result)


class CreateUserView(View):
    service = UserService
    form = UserForm
    decorators = [admin_required(), login_required("user")]

    async def post(self, request, user):
        form = self.form(data=request.json)
        if form.validate():
            service = self.service()
            try:
                new_user = await service.create_user(form)
                return self.success(new_user)
            except ModelUniqueException as e:
                logger.error(f"ModelUniqueException: 用户名必须唯一,{e}")
                return self.fail("用户名必须唯一")
        return self.fail(form.errors)


class DeleteUserView(View):
    service = UserService
    decorators = [admin_required(), login_required("user")]

    async def post(self, request, user_id, user):
        service = self.service()
        try:
            await service.delete_user(user_id)
            return self.success("成功")
        except Exception as e:
            return self.fail("删除出现错误")
