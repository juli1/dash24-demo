from flask import Flask, request, jsonify

import database as db
from model import Product

app = Flask(__name__)

db_connection = db.connect_database()

@app.route("/api/product/list", methods=["GET"])
def product_list():
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    products = db.get_products(db_connection, limit, offset)
    return jsonify(products)


@app.route("/api/product/add", methods=["POST"])
def product_add():
    product_json = request.json
    product = Product(0, product_json["name"])

    success = db.add_product(db_connection, product)
    if success:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "product already exists"}), 500