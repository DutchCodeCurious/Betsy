from model import (Product, Tag, Product_Tag)


def add_tag_to_product(p_id, tag_name):
    try:
        product = Product.get_by_id(p_id)

        tag = Tag.get_or_none(name=tag_name)
        if not tag:
            tag = Tag.create(name=tag_name)

        product_tag = Product_Tag.get_or_none(product=product, tag=tag)
        if not product_tag:
            product_tag = Product_Tag.create(product=product, tag=tag)

        print(
            f"Tag '{tag_name}' added to product {product.name} successfully.")
    except Product.DoesNotExist:
        print(f"Product with ID '{p_id}' does not exist.")
