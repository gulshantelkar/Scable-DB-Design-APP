from peewee import Model
from database import database
from peewee import *
from playhouse.postgres_ext import *
from fastapi import HTTPException
import datetime


class BaseModel(Model):
    class Meta:
        database = database
        only_save_dirty = True

class Tag(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True)
    tag_name = CharField(index=True)
    created_at = DateTimeField(default=datetime.datetime.now, index=True)
    updated_at = DateTimeField(default=datetime.datetime.now, index=True)

    
    class Meta:
        table_name = 'tags'
        
