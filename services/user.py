from models.user import UserModel


class UserService(object):
    model = UserModel

    async def create_user(self, username, password):
        pass

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

    async def verify_token(self, token):
        user = await self.model.find_one({"token": token})
        if user:
            return True, user
        else:
            return False, None

    async def add_role(self, role_key):
        pass
