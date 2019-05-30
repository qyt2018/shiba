from sanic_motor import BaseModel
from exceptions.model import ModelUniqueException


class Model(BaseModel):

    @classmethod
    async def insert_one(cls, doc, **kwargs):
        db = kwargs.pop('db', None)
        is_uniq = await cls.is_unique(doc=doc)
        if is_uniq in (True, None):
            return await cls.get_collection(db).insert_one(doc, **kwargs)
        raise ModelUniqueException()

    @classmethod
    async def insert_many(cls, *args, **kwargs):
        db = kwargs.pop('db', None)
        return await cls.get_collection(db).insert_many(*args, **kwargs)
