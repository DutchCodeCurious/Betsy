import peewee as pw
from datetime import datetime

p = "betsy.db"
db = pw.SqliteDatabase(p)
db.connect()
vandaag = datetime.now().strftime("%d-%m-%y %H:%M:%S")


class User(pw.Model):
    user_name = pw.CharField(unique=True)
    address = pw.CharField()
    bank_account = pw.CharField(unique=True, max_length=50)
    created_at = pw.DateTimeField(
        default=datetime.now().strftime("%d-%m-%y %H:%M:%S"))

    class Meta:
        database = db


class Tag(pw.Model):
    name = pw.CharField(unique=True)

    class Meta:
        database = db


class Product(pw.Model):
    user_id = pw.ForeignKeyField(User)
    name = pw.CharField()
    desc = pw.TextField()
    price = pw.DecimalField(max_digits=10, decimal_places=2)
    quantity = pw.IntegerField()

    class Meta:
        database = db


class Product_Tag(pw.Model):
    product = pw.ForeignKeyField(Product, backref='product_tags')
    tag = pw.ForeignKeyField(Tag, backref='tag_products')

    class Meta:
        database = db


class Inventory(pw.Model):
    user_id = pw.ForeignKeyField(User)
    product_id = pw.ForeignKeyField(Product)

    class Meta:
        database = db


class Order(pw.Model):
    buyer_id = pw.ForeignKeyField(User)
    product_id = pw.ForeignKeyField(Product)

    class Meta:
        database = db


class Pay_details(pw.Model):
    order_id = pw.ForeignKeyField(Order)
    seller_id = pw.ForeignKeyField(User)
    price = pw.DecimalField(max_digits=10, decimal_places=2)
    quantity = pw.IntegerField()
    sold_at = pw.DateTimeField(
        default=datetime.now().strftime("%d-%m-%y %H:%M:%S"))

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([User, Product, Tag,
                         Inventory, Order, Pay_details, Product_Tag])


if __name__ == "__main__":
    create_tables()
