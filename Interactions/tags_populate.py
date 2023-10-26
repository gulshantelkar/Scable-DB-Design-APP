import json
from models.tags import Tag  

def tags_populate():
    json_file_path = '/Users/gulshantelkar/Desktop/Assignment/kopari_products.json'

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    products = data.get('products', [])

    all_tags = set()  

    for product_data in products:
        tags = product_data.get('tags', [])

        for tag in tags:
            all_tags.add(tag) 


    for tag_name in all_tags:
        Tag.get_or_create(tag_name=tag_name)

