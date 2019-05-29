from sanic_motor import BaseModel
import hashlib
import uuid


class UserModel(BaseModel):
    __coll__ = "user"
    __unique_fields__ = ["username"]

    def create_token(self):
        return uuid.uuid4().hex

    def verify_password(self, password):
        hash_password = self.hash_password(password)
        if hash_password == self.password:
            return True
        else:
            return False

    def hash_password(self, password):
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        return md5.hexdigest()
