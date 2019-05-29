from services.user import UserService
from sanic.response import json


def login_required(user_keyword):
    def decorator(func):
        async def decorator_function(request, *args, **kwargs):
            service = UserService()
            state, user = await service.verify_token(request.token)
            if state:
                kwargs[user_keyword] = user
                return await func(request, *args, **kwargs)
            else:
                return json({"msg": "认证失败", "code": 401, "result": "未登录"})

        return decorator_function

    return decorator


def hash_roles():
    pass
