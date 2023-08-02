```python
from flask import flash
from website_project.models import User, Product, Order

def flash_messages(message_name):
    messages = {
        "loginSuccess": "Successfully logged in!",
        "registerSuccess": "Successfully registered!",
        "orderPlaced": "Your order has been placed!"
    }
    flash(messages.get(message_name, "An error occurred."))

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user

def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    return product

def get_order_by_id(order_id):
    order = Order.query.get(order_id)
    return order

def calculate_total_order_cost(order_id):
    order = get_order_by_id(order_id)
    total_cost = sum([product.price for product in order.products])
    return total_cost
```