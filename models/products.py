from peewee import Model
from playhouse.postgres_ext import UUIDField
from database import database
from peewee import *
import datetime
from models.vendors import Vendor
from models.product_type import ProductType

class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class Product(BaseModel):
    id = CharField(index=True, primary_key=True)
    title = CharField(index=True)
    handle = CharField(index=True)
    body_html = TextField()  
    published_at = DateTimeField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    vendor_id=ForeignKeyField(Vendor, to_field="id")
    product_type_id=ForeignKeyField(ProductType, to_field="id")
    
    class Meta:
        table_name = 'product'
