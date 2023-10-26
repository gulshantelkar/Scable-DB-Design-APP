from models.vendors import Vendor
from models.image_product_mapping import ImageProductMapping
from models.product_type import ProductType
from models.products import Product
from models.tag_product_mapping import TagProductMapping
from models.tags import Tag
from models.variant_product_mapping import VariantProductMapping
from models.option_product_mapping import OptionProdcutMapping

def list_products(page, size,title,handle,product_type,vendor_name,product_id,tags):
    query = Product.select()

    if title:
        query = query.where(Product.title.contains(title))
    if handle:
        query = query.where(Product.handle.contains(handle))
    if product_type:
        product_type_entry = ProductType.get_or_none(ProductType.product_type == product_type)
        if product_type_entry:
            query = query.where(Product.product_type_id == product_type_entry.id)
    if vendor_name:
        vendor_entry = Vendor.get_or_none(Vendor.vendor_name == vendor_name)
        if vendor_entry:
            query = query.where(Product.vendor_id == vendor_entry.id)
    if product_id:
        query = query.where(Product.id == product_id)

    if tags:
        tag_list = tags.split(",")
        subquery = TagProductMapping.select(TagProductMapping.product_id).join(Tag).where(
            Tag.tag_name.in_(tag_list)
        )
        query = query.where(Product.id << subquery)

    query = query.paginate(page, size)

    products = query.execute()

    formatted_products = []
    for product in products:
        formatted_product = {
            "id": product.id,
            "title": product.title,
            "handle": product.handle,
            "body_html": product.body_html,
            "published_at": str(product.published_at),
            "created_at": str(product.created_at),
            "updated_at": str(product.updated_at),
            "vendor": Vendor.get(Vendor.id == product.vendor_id).vendor_name,
            "product_type": ProductType.get(ProductType.id == product.product_type_id).product_type,
            "tags": [tag.tag_name for tag in Tag.select().join(TagProductMapping).where(TagProductMapping.product_id == product.id)],
            "variants": [
                {
                    "id": variant.id,
                    "title": variant.title,
                    "option1": variant.option1,
                    "option2": variant.option2,
                    "option3": variant.option3,
                    "sku": variant.sku,
                    "requires_shipping": variant.requires_shipping,
                    "taxable": variant.taxable,
                    "featured_image": variant.featured_image,
                    "available": variant.available,
                    "price": variant.price,
                    "grams": variant.grams,
                    "compare_at_price": variant.compare_at_price,
                    "position": variant.position,
                    "created_at": str(variant.created_at),
                    "updated_at": str(variant.updated_at),
                }
                for variant in VariantProductMapping.select().where(VariantProductMapping.product_id == product.id)
            ],
            "images": [
                {
                    "id": image.id,
                    "position": image.position,
                    "src": image.src,
                    "width": image.width,
                    "height": image.height,
                    "created_at": str(image.created_at),
                    "updated_at": str(image.updated_at),
                }
                for image in ImageProductMapping.select().where(ImageProductMapping.product_id == product.id)
            ],
            "options": [
                {
                    "id": option.id,
                    "name": option.name,
                    "position": option.position,
                    "values": option.values
                }
                for option in OptionProdcutMapping.select().where(OptionProdcutMapping.product_id == product.id)
            ],
        }
        formatted_products.append(formatted_product)

    return {"products": formatted_products}
