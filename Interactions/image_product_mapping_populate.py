import json
from datetime import datetime
from models.products import Product
from models.image_product_mapping import ImageProductMapping

def image_product_mapping_populate():

    json_file_path = '/Users/gulshantelkar/Desktop/Assignment/kopari_products.json'

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        
    products = data.get('products', [])
    
    for product_data in products:
        images = product_data.get('images', [])

        for image_data in images:
            id = image_data.get('id')
            position = image_data.get('position')
            src = image_data.get('src')
            width = image_data.get('width')
            height = image_data.get('height')
            product_id = image_data.get('product_id')

            ImageProductMapping.create(
                    id=id,
                    position=position,
                    src=src,
                    width=width,
                    height=height,
                    product_id=product_id
                )



