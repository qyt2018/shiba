from sanic_motor import BaseModel
from exceptions.model import ModelUniqueException
import math


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

    @classmethod
    async def page_find(cls, request=None, *args, **kwargs):
        page_name = kwargs.pop('page_name', 'page')
        per_page_name = kwargs.pop('per_page_name', 'per_page')
        page, per_page, skip = cls.get_page_args(request, page_name,
                                                 per_page_name, **kwargs)
        cur = await super(Model, cls).find(request, *args, **kwargs)
        doc_count = await cls.count_documents(*args, **kwargs)
        page_count = math.ceil(doc_count / per_page)
        return {'page_count': page_count, 'objects': cur.objects}
