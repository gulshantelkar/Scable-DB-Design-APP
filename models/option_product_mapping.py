from peewee import Model, ForeignKeyField
from playhouse.postgres_ext import UUIDField, JSONField,ArrayField
from database import database
from peewee import *
import datetime
from models.products import Product

class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class OptionProdcutMapping(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True,index=True)
    product_id = ForeignKeyField(Product,to_field='id')
    name =  CharField(index=True,null =True)
    position =  IntegerField(index=True)
    values=ArrayField(CharField,null=True)

    class Meta:
        table_name = 'option_product_mapping'
