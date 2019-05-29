from utils.view import View
from services.user import UserService
from forms.user import LoginForm
from utils.auth import login_required


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


class UserListView(View):
    service = UserService
    decorators = [login_required("user")]

    async def get(self, request, user):
        return self.success("成功")

    async def post(self, request, user):
        return self.success("成功")
