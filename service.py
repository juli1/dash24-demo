from flask import Flask, request, jsonify, render_template, render_template_string
import logging
import database as db
from model import Product

app = Flask(__name__)

db_connection = db.connect_database()

# API to get the list of products
@app.route("/api/product/list", methods=["GET"])
def apiProduct_list():
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    products = db.get_products(db_connection, limit, offset)
    assert(len(products)>0)
    return jsonify(products)


# API to add a product
@app.route("/api/product/add", methods=["POST"])
def apiProduct_add():
    product_json = request.json
    product = Product(0, product_json["name"])

    # Logging should not have the format string. Just use
    # logging.info("adding product %s", product.name)
    logging.info("adding product {0}".format(product.name)) 
    success = db.add_product(db_connection, product)

    # The else is not necessary here, we can remove it.
    if success:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "product already exists"}), 500

# API to list all products with an endpoint
@app.route("/product/list", methods=["GET"])
def product_list():
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    products = db.get_products(db_connection, limit, offset)
    return render_template('product_list.html', limit=limit, offset=offset, products=products)


# Index
@app.route("/", methods=["GET"])
def index():
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    products = db.get_products(db_connection, limit, offset)
    # render_template_string may contains some injection. Prefer to use templates in files instead.
    # See https://docs.datadoghq.com/code_analysis/static_analysis_rules/python-flask/no-render-template-string/
    # replace with the following
    # return render_template("index.html")
    return render_template_string("<html><body><a href=\"/product/list\">product list</a></body></html>")

# Your application should never run on all interfaces.
# See https://docs.datadoghq.com/code_analysis/static_analysis_rules/python-flask/listen-all-interfaces/
# Bind to localhost for development purposes and attach to the address 127.0.0.1
# Replace with the following
# app.run(host="127.0.0.1")
app.run(host="0.0.0.0")