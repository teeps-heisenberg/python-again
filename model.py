from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,String, Integer, Float

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)


    #For Mapping of Object in Response
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }