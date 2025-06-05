from flask import Flask
from products import products_boilerplate
from model import Product,db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(products_boilerplate, url_prefix="/products")

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)