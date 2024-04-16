from flask import Flask, request, jsonify

import database as db
app = Flask(__name__)

db_connection = db.connect_database()

@app.route("/product/list", methods=["GET"])
def product_list():
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    products = db.get_products(db_connection, limit, offset)
    return jsonify(products)


