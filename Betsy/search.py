from model import (User, Product, Product_Tag, Tag,)
from peewee import fn
from tabulate import tabulate


def product_id(product, user_name):
    us_id = user_id(user_name)
    item = Product.select(Product.id).where(
        (fn.lower(Product.name) == product.lower()) &
        (Product.user_id == us_id)).limit(1)
    result = item.scalar()
    return result


def user_id(user_name):
    query = User.select(User.id).where(
        fn.lower(User.user_name) == user_name.lower()).limit(1)
    result = query.scalar()
    if result is None:
        return None
    else:
        return result


def product_price(p_id):
    query = Product.select(Product.price).where(
        Product.id == p_id).limit(1)
    result = query.scalar()
    return result


def user_search(search):
    us_id = user_id(search)
    if us_id is None:
        return ValueError
    else:
        print("Found")


def tag_search(search):
    tag_id = Tag.select(Tag.id).where(Tag.name == search)
    product = (Product
               .select()
               .join(Product_Tag)
               .where(Product_Tag.id == tag_id))
    print(product)


def search_products_by_tag(tag_name):
    try:
        tag = Tag.get(Tag.name == tag_name)

        products = (Product
                    .select()
                    .join(Product_Tag)
                    .where(Product_Tag.tag == tag))

        return list(products)

    except Tag.DoesNotExist:
        print(f"Tag '{tag_name}' does not exist.")
        return []


def poducts_by_tag(tag_name):
    product = search_products_by_tag(tag_name)
    table_data = []
    for prod in product:
        table_data.append([prod.name, prod.desc,
                          prod.price, prod.quantity])

    if table_data:
        headers = ["Name", "Description", "Price", "Quantity"]
        table = tabulate(table_data, headers, tablefmt="grid")
        print(table)
    else:
        print(f"No products found with tag '{tag_name}'.")
