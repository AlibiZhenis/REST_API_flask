from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


prod_schema = ProductSchema()
prods_schema = ProductSchema(many=True)

@app.route('/product', methods=["POST"])
def add_product():
    name = request.json['name']
    desc = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, desc, price, qty)
    db.session.add(new_product)
    db.session.commit()

    return prod_schema.jsonify(new_product)


@app.route('/product', methods=["GET"])
def get_all_products():
    all_products = Product.query.all()
    result = prods_schema.dump(all_products)
    return jsonify(result)


@app.route('/product/<id>', methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    return prod_schema.jsonify(product)


@app.route('/product/<id>', methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    desc = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = desc
    product.price = price
    product.qty = qty

    db.session.commit()

    return prod_schema.jsonify(product)


@app.route('/product/<id>', methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return prod_schema.jsonify(product)


if __name__ == '__main__':
    app.run(debug=True)
