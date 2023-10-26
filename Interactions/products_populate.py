
from models.products import Product
from models.product_type import ProductType
from models.vendors import Vendor
from datetime import datetime
import json

def parse_date(date_str):
    date_format = '%Y-%m-%dT%H:%M:%S%z'

    try:
        return datetime.strptime(date_str, date_format)
    except ValueError:
        return None  
def parse_date(date_str):
    date_format = '%Y-%m-%dT%H:%M:%S%z'

    try:
        return datetime.strptime(date_str, date_format)
    except ValueError:
        return None  

def products_populate():
    json_file_path = '/Users/gulshantelkar/Desktop/Assignment/kopari_products.json'


    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    products = data.get('products', [])

    for product_data in products:
        product_id=product_data.get('id')
        title = product_data.get('title')
        handle = product_data.get('handle')
        body_html = product_data.get('body_html')
        published_at = product_data.get('published_at')
        vendor_name = product_data.get('vendor')
        product_type_name = product_data.get('product_type')
        published_at = parse_date(product_data.get("published_at"))

        vendor = Vendor.select().where(Vendor.vendor_name == vendor_name).first()


        if vendor:
            vendor_id = vendor.id

        product_type = ProductType.select().where(ProductType.product_type == product_type_name).first()


        if product_type:
            product_type_id = product_type.id

        Product.create(
            id=product_id,
            title=title,
            handle=handle,
            body_html=body_html,
            published_at=published_at,
            vendor_id=vendor_id,
            product_type_id=product_type_id,
    
        )




