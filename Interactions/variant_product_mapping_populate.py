import json
from models.variant_product_mapping import VariantProductMapping
from models.products import Product
from datetime import datetime

def variant_product_mapping_populate():
    with open('/Users/gulshantelkar/Desktop/Assignment/kopari_products.json', 'r') as json_file:
        data = json.load(json_file)

    for product_data in data.get("products", []):
        product_id = product_data.get("id")
        variants = product_data.get("variants")

        product = Product.get(Product.id == product_id)


        if variants:
            for variant_data in variants:
                compare_at_price = float(variant_data.get("compare_at_price")) if variant_data.get("compare_at_price") else 0.0

                VariantProductMapping.create(
                    product_id=product,
                    title=variant_data.get("title"),
                    option1=variant_data.get("option1"),
                    option2=variant_data.get("option2"),
                    option3=variant_data.get("option3"),
                    sku=variant_data.get("sku"),
                    requires_shipping=variant_data.get("requires_shipping"),
                    taxable=variant_data.get("taxable"),
                    featured_image=variant_data.get("featured_image"),
                    available=variant_data.get("available"),
                    price=float(variant_data.get("price")),
                    grams=variant_data.get("grams"),
                    compare_at_price=compare_at_price,  
                    position=variant_data.get("position")
                )
