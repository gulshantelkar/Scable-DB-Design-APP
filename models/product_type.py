from peewee import Model
from database import database
from peewee import *
from playhouse.postgres_ext import *
import datetime


class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class ProductType(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True)
    product_type = CharField(index=True)
    status = CharField(default='active', index=True)
    created_at = DateTimeField(default=datetime.datetime.now, index=True)
    updated_at = DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        table_name = 'product_type'

