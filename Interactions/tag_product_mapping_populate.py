import json
from models.tag_product_mapping import TagProductMapping
from models.tags import Tag
from models.products import Product

def tag_product_mapping_populate():

    json_file_path = '/Users/gulshantelkar/Desktop/Assignment/kopari_products.json'

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    products = data.get('products', [])

    for product_data in products:
        product_id = product_data.get('id')
        tags = product_data.get('tags', [])

        for tag in tags:
            tag_entry, created = Tag.get_or_create(tag_name=tag)

            mapping_exists = TagProductMapping.select().where(
                (TagProductMapping.product_id == product_id) &
                (TagProductMapping.tag_id == tag_entry.id)
            ).exists()

            if not mapping_exists:
                TagProductMapping.create(
                    product_id=product_id,
                    tag_id=tag_entry.id
                )
