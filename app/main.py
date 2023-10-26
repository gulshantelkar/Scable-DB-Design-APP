from fastapi import FastAPI

from params import *
from fastapi import HTTPException
from uuid import UUID
from app.__init__ import json_encoder
from fastapi.responses import JSONResponse
from fastapi import Query
from database import database
from models.vendors import Vendor
from models.image_product_mapping import ImageProductMapping
from models.product_type import ProductType
from models.products import Product
from models.tag_product_mapping import TagProductMapping
from models.tags import Tag
from models.variant_product_mapping import VariantProductMapping
from models.option_product_mapping import OptionProdcutMapping
from peewee import JOIN
from Interactions.list_vendors import list_vendors
from Interactions.product_type_populate import product_type_populate
from Interactions.image_product_mapping_populate import image_product_mapping_populate
from Interactions.option_product_mapping_populate import option_product_mapping_populate
from Interactions.variant_product_mapping_populate import variant_product_mapping_populate
from Interactions.tag_product_mapping_populate import tag_product_mapping_populate
from Interactions.tags_populate import tags_populate
from Interactions.products_populate import products_populate
from Interactions.list_products import list_products
from Interactions.get_product import get_product


app = FastAPI()

with database:
    database.create_tables([ImageProductMapping,ProductType,Product,TagProductMapping,Tag,VariantProductMapping,OptionProdcutMapping,Vendor]) 


# product_type_populate()
# image_product_mapping_populate()
# products_populate()
# option_product_mapping_populate()
# variant_product_mapping_populate()
# tags_populate()(
# tag_product_mapping_populate()

@app.post("/vendors/")
async def create_vendor(request: VendorCreate):
    vendor = Vendor.create(
        vendor_name=request.vendor_name,
        status=request.status
    )
    return vendor


@app.get("/vendors/{vendor_id}")
async def read_vendor(vendor_id: UUID):
    try:
        vendor = Vendor.get(Vendor.id == vendor_id)
    except Vendor.DoesNotExist:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor

@app.get("/vendors/")
async def list_vendors_data(page: int = 1, page_limit: int = 10):
    try:
        data = list_vendors(page, page_limit)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
    
from fastapi import HTTPException

@app.get("/products/{product_id}", response_model=dict)
async def get_product_data(product_id: str):
    try:
        product_data = get_product(product_id)
        if product_data:
            return product_data
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/products")
async def list_products_data(
    page: int = Query(1, title="Page number", description="The page number for paginating results."),
    size: int = Query(10, title="Page size", description="The number of items per page."),
    title: str = Query(None, title="Filter by product title"),
    handle: str = Query(None, title="Filter by product handle"),
    product_type: str = Query(None, title="Filter by product type"),
    vendor_name: str = Query(None, title="Filter by vendor name"),
    product_id: str = Query(None, title="Filter by product ID"),
    tags: str = Query(None, title="Filter by tags (comma-separated)"),
):
    try:
        data = list_products(page, size,title,handle,product_type,vendor_name,product_id,tags)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
    