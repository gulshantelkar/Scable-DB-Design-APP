from peewee import Model, ForeignKeyField
from playhouse.postgres_ext import UUIDField, JSONField
from database import database
from peewee import *
import datetime
from models.products import Product

class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class VariantProductMapping(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True,index=True)
    product_id = ForeignKeyField(Product,to_field='id')
    title =  CharField(index=True,null =True)
    option1 =  CharField(index=True,null =True)
    option2 =  CharField(index=True,null =True)
    option3 =  CharField(index=True,null =True)
    sku =  CharField(index=True)
    requires_shipping = BooleanField()
    taxable = BooleanField()
    featured_image = TextField(index=True,null =True)
    available = BooleanField()
    price = FloatField()
    grams = IntegerField()
    compare_at_price = FloatField(default=0.0)
    position = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now, index=True)
    updated_at = DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        table_name = 'variant_product_mapping'

