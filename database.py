import sqlite3
from model import Product
DATABASE_FILE = "db.sqlite"

def connect_database():
    con = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
    return con

def get_products(db_connection, limit, offset):
    products = []
    cursor = db_connection.cursor()
    res = cursor.execute("SELECT id, title from products")
    for v in res:
        products.append(Product(v[0], v[1]))

    return products[offset:offset+limit]


def add_product(db_connection, product: Product):
    try:
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO products (id, title) VALUES (NULL, '" + product.name+"');")
        db_connection.commit()
        return True
    # NIY replace with sqlite3.IntegrityError
    except Exception as e:
        return False
