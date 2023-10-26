from peewee import Model
from playhouse.postgres_ext import UUIDField, JSONField, ArrayField, SQL
from database import database
from peewee import *
from fastapi import HTTPException
import datetime
from models.tags import Tag
from models.products import Product

class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class TagProductMapping(BaseModel):
    id = UUIDField(index=True, primary_key=True, constraints=[SQL("DEFAULT gen_random_uuid()")])
    product_id = ForeignKeyField(Product, to_field="id",index=True)
    tag_id = ForeignKeyField(Tag,to_field="id",index=True)

    class Meta:
        table_name = 'tag_product_mapping'
