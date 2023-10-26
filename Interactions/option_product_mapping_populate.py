import json
from datetime import datetime
from models.products import Product
from models.option_product_mapping import OptionProdcutMapping

def option_product_mapping_populate():

    json_file_path = '/Users/gulshantelkar/Desktop/Assignment/kopari_products.json'

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    products = data.get('products', [])

    for product_data in products:
        options = product_data.get('options', [])

        for option_data in options:
            product_id = product_data.get('id')
            name = option_data.get('name')
            position = option_data.get('position')
            values = option_data.get('values')

            OptionProdcutMapping.create(
                product_id=product_id,
                name=name,
                position=position,
                values=values
            )

