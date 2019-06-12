from models.user import UserModel
from forms.user import UserForm


class UserService(object):
    model = UserModel

    def get_user_result(self, user):
        result = {
            "id": str(user.id),
            "name": user.name,
            "username": user.username,
            "is_admin": user.is_admin,
            "scope": ["user"]
        }
        if user.is_admin:
            result['scope'].append("admin")
        return result

    async def user_by_id(self, id):
        user = await self.model.find_one(id)
        if user:
            return user
        return False

    async def find_users(self, filter):
        users = await self.model.find(filter)
        return map(self.get_user_result, users.objects)

    async def create_user(self, user_form: UserForm):
        user_data = {
            "name": user_form.name.data,
            "username": user_form.username.data,
            "is_admin": user_form.is_admin.data,
            "password": self.model().hash_password(user_form.password.data)
        }
        user = await self.model.insert_one(user_data)
        return str(user.inserted_id)

    async def delete_user(self, user_id):
        user = await self.model.find_one(user_id)
        state = await user.destroy()
        if state.deleted_count >= 1:
            return state
        else:
            raise Exception()

    async def authentication(self, username, password):
        user = await self.model.find_one({"username": username})
        if user:
            if user.verify_password(password):
                token = user.create_token()
                await self.model.update_one({u'_id': user.id}, {'$set': {"token": token}})
                return True, token
            else:
                return False, "密码错误"
        else:
            return False, "未找到用户"

    async def logout(self, user):
        await self.model.update_one({u'_id': user.id}, {'$set': {"token": None}})

    async def verify_token(self, token):
        user = await self.model.find_one({"token": token})
        if user:
            return True, user
        else:
            return False, None
