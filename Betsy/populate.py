from model import (db, User, Product, Inventory, Order,
                   Pay_details, Tag, Product_Tag)
from main import new_product
from add import add_tag_to_product


user0 = {
    "user_name": "Mark_Rutte",
    "address": "Binnenhof 1",
    "bank_account": "NL20INGB003350709"
}
user1 = {
    "user_name": "Geertje_Wilders",
    "address": "Afgesloten 2",
    "bank_account": "NL10RABO001250890"
}
user2 = {
    "user_name": "Karel_deGroot",
    "address": "Slot Gouda 1",
    "bank_account": "NL1500Staat010912"
}
user3 = {
    "user_name": "Frans_deWaal",
    "address": "Parijs eiffel 10",
    "bank_account": "FR17ABN102330321"
}
user4 = {
    "user_name": "Joppe_Petit",
    "address": "Paleis Noordeinde 1",
    "bank_account": "NLINGB00022507262"
}

user5 = {
    "user_name": "Linde_Petit",
    "address": "Rotterdam erg. 10",
    "bank_account": "NLINGB00033684943"
}

user6 = {
    "user_name": "Najib_Amhali",
    "address": "De goot",
    "bank_account": "NLABN3200092331"
}

user7 = {
    "user_name": "Sigrid_Kaag",
    "address": "Den haag, bij fakkel",
    "bank_account": "NLINGBDESTAAT001"
}

user8 = {
    "user_name": "Klaasjan_Huntelaar",
    "address": "Amsterdam Arena",
    "bank_account": "NLAJAX0012394239"
}

users = [user0, user1, user2, user3, user4, user5, user6, user7, user8]


def populate_betsy():
    with db:
        db.create_tables([User, Product, Inventory, Order,
                         Pay_details, Tag, Product_Tag])

    with db.atomic():
        User.insert_many(users).execute()


def products_betsy():
    new_product("Linde_Petit", "Samsung s10", "tech",
                "Zo goed als kapot", 150, 1)
    new_product("Joppe_Petit", "Iphone 14", "tech",
                "Nog helemaal nieuw", 780, 1)
    new_product("Mark_Rutte", "Fiets", "transport",
                "Gestolen van de koning", 180, 1)
    new_product("Klaasjan_Huntelaar", "Wok", "Kitchen gadget",
                "Stalen wok, hout handvat", 24.95, 6)
    new_product("Karel_deGroot", "Boeken kist", "Storing",
                "Ruimte voor een volwassen persoon", 499, 1)
    new_product("Linde_Petit", "Kaas", "Food",
                "De lekkerste uit Rotterdam", 9.80, 5)
    new_product("Mark_Rutte", "Kaas", "Food",
                "De lekkerste uit Den Haag", 19.50, 9)
    new_product("Joppe_Petit", "Stoel", "hout",
                "Zelf gemaakt", 59.90, 1)
    new_product("Joppe_Petit", "Granola", "Food",
                "Ontbijt spul", 1.99, 4)
    new_product("Joppe_petit", "test", "test", "test", 99.99, 1)


def extra_product_tags():
    add_tag_to_product(8, "zitwaar")
    add_tag_to_product(9, "Ontbijt")


if __name__ == "__main__":
    populate_betsy()
    products_betsy()
    extra_product_tags()
