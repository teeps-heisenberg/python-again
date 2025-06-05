from flask import Blueprint,jsonify, request
from model import Product,db

products_boilerplate = Blueprint('products',__name__)



@products_boilerplate.route('/',methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products]), 200

@products_boilerplate.route('/',methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error":"Missing Required Params"}), 400

    product = Product(name = data["name"], price = data["price"])
    db.session.add(product)
    db.session.commit()

    return jsonify(product.to_dict()), 201