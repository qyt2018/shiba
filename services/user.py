from models.user import UserModel
from forms.user import UserForm


class UserService(object):
    model = UserModel

    async def find_users(self, filter):
        users = await self.model.find(filter)
        return users.objects

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
        pass

    async def authentication(self, username, password):
        user = await self.model.find_one({"username": username})
        if user.verify_password(password):
            token = user.create_token()
            await self.model.update_one({u'_id': user.id}, {'$set': {"token": token}})
            return True, token
        else:
            return False, None

    async def logout(self, user):
        await self.model.update_one({u'_id': user.id}, {'$set': {"token": None}})

    async def verify_token(self, token):
        user = await self.model.find_one({"token": token})
        if user:
            return True, user
        else:
            return False, None
