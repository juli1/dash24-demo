import sqlite3
import tenacity
import logging
from model import Product
DATABASE_FILE = "db.sqlite"

@tenacity.retry(wait=tenacity.wait_fixed(5))
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
        # This is a potential SQL injection as the product nme is potentially directly passed from the user.
        # replace with 
        # cursor.execute("INSERT INTO products (id, title) VALUES (NULL, ?)", (product.name, ))
        cursor.execute("INSERT INTO products (id, title) VALUES (NULL, '" + product.name+"');")
        db_connection.commit()
        return True
    # a bare exception fails to captures the exact exceptions (and print it). The code should rather
    # catch specific exceptions.
    # https://docs.datadoghq.com/code_analysis/static_analysis_rules/python-best-practices/no-bare-except/
    # replace with
    # # except sqlite3.IntegrityError:
    except:
        return False
