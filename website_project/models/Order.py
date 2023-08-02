from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from website_project.utils.database import Base
from website_project.models.User import User
from website_project.models.Product import Product
import datetime

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

User.orders = relationship('Order', order_by=Order.id, back_populates='user')
Product.orders = relationship('Order', order_by=Order.id, back_populates='product')