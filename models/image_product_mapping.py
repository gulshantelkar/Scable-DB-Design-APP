from peewee import Model
from database import database
from peewee import *
from fastapi import HTTPException
import datetime
from models.products import Product  

class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class ImageProductMapping(BaseModel):
    id = CharField(index=True, primary_key=True)
    position = IntegerField(index=True) 
    src = CharField(index=True)  
    width = IntegerField()
    height = IntegerField()
    product_id = ForeignKeyField(Product,to_field="id")
    created_at = DateTimeField(default=datetime.datetime.now, index=True)
    updated_at = DateTimeField(default=datetime.datetime.now, index=True)
    

    class Meta:
        table_name = 'image_product_mapping'
