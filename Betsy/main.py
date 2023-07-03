from model import (User, Product, Inventory, Order,
                   Pay_details, Tag, Product_Tag)
from search import (product_id, user_id, product_price, search_products_by_tag)
from peewee import fn
from tabulate import tabulate


def product_search(search):
    target = Product.select().where(
        fn.lower(Product.name) ** f'%{search.lower()}%')
    table_data = []

    if target.count() == 0:
        return ValueError(f"There is no product called {search}")

    else:
        for prod in target:
            table_data.append([prod.name, prod.desc,
                               prod.price, prod.quantity])
        if table_data:
            headers = ["Name", "Description", "Price", "Quantity"]
            table = tabulate(table_data, headers,
                             tablefmt="grid")
            title = f"Products search by: {search}"
            table_with_title = f"\n{title}\n{table}\n"

        print(table_with_title)


def poducts_by_tag(tag_name):
    product = search_products_by_tag(tag_name)
    table_data = []
    for prod in product:
        table_data.append([prod.name, prod.desc,
                          prod.price, prod.quantity])

    if table_data:
        headers = ["Name", "Description", "Price", "Quantity"]
        table = tabulate(table_data, headers, tablefmt="grid")

        title = f"Products by the tag: {tag_name}"
        table_with_title = f"\n{title}\n{table}\n"

        print(table_with_title)
    else:
        print(f"No products found with tag '{tag_name}'.")


def user_products(user):
    us_id = user_id(user)
    target = Product.select().where(Product.user_id == us_id)
    table_data = []

    if target.count() == 0:
        return ValueError(f"{user} has no products")
    else:
        for prod in target:
            table_data.append([prod.name, prod.desc,
                               prod.price, prod.quantity])
    if table_data:
        headers = ["Name", "Description", "Price", "Quantity"]
        table = tabulate(table_data, headers,
                         tablefmt="grid")

        title = f"Products of user: {user}"
        table_with_title = f"\n{title}\n{table}\n"
        print(table_with_title)


def update_stock(user, product, amount):
    p_id = product_id(product, user)

    if p_id is None:
        return print(f"{user} does not have {product}")

    target = Product.get((Product.id == p_id))
    if amount == 0:
        remove_product(user, product)
    else:
        target.quantity = amount
    target.save()

    print(
        f"{product} is updated successfully by {user}, quantity is {amount}")


def remove_product(user, product):
    p_id = product_id(product, user)

    if p_id is None:
        return print(f"{user} does not have {product}")

    target = Inventory.get((Inventory.product_id == p_id))
    target.delete_instance()
    print(f"{product} deleted from inventory.")

    target = Product.get((Product.id == p_id))
    target.delete_instance()
    print(f"{product} deleted by {user}.")


def new_product(user, product, tag, description, price, amount):
    tag = tag.lower()
    existing_tag = Tag.select().where((Tag.name) == tag).first()

    if existing_tag is None:
        tags = Tag(
            name=tag
        )
        tags.save()

    id = User.select(User.id).where(fn.lower(User.user_name) == user.lower())
    tag_id = Tag.select(Tag.id).where(Tag.name == tag)
    prod = Product(
        user_id=id,
        name=product,
        desc=description,
        price=price,
        quantity=amount
    )
    prod.save()

    inventory = Inventory(
        user_id=id,
        product_id=prod.id
    )
    inventory.save()

    p_tags = Product_Tag(
        product=prod.id,
        tag=tag_id
    )

    p_tags.save()

    print(f"{product} successfully added to {user}.")


def buy_product(buyer, seller, product, amount):
    buyer_id = user_id(buyer)
    seller_id = user_id(seller)
    p_id = product_id(product, seller)

    if buyer_id is None:
        return print(f"{buyer} does not exist")
    if seller_id is None:
        return print(f"{seller} does not exist")
    if p_id is None:
        return print(f"{product} is not in stock by {seller}")

    target = Product.get((Product.id == p_id))
    if target.quantity < amount:
        return print(
            f"Seller: {seller} does not have {amount} units of {product}")

    price = product_price(p_id)
    order = Order(
        buyer_id=buyer_id,
        product_id=p_id
    )
    order.save()

    details = Pay_details(
        order_id=order,
        seller_id=seller_id,
        price=(amount * price),
        quantity=amount,
    )
    details.save()

    target.quantity = target.quantity - amount
    target.save()

    print(f"{buyer} successfully bought {amount} {product} from {seller}.")


# ALL TEST ACTIONS
# KEEP HASHED WHILE POPULATING

# poducts_by_tag("food")
# user_products("Joppe_petit")
# product_search("k")
# remove_product("Joppe_petit", "test")
# update_stock("linde_petit", "kaas", 25)
# buy_product("joppe_petit", "linde_petit", "kaas", 2)
# new_product("Joppe_Petit", "paprika", "food", "groenten", 0.99, 9)
