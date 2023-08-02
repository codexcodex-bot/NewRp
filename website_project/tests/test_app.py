import unittest
from website_project.app import create_app
from website_project.models.User import User
from website_project.models.Product import Product
from website_project.models.Order import Order
from website_project.utils.database import db

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_product_page(self):
        response = self.client.get('/product/1')
        self.assertEqual(response.status_code, 404)  # No product with id 1

    def test_cart_page(self):
        response = self.client.get('/cart')
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_checkout_page(self):
        response = self.client.get('/checkout')
        self.assertEqual(response.status_code, 302)  # Redirect to login page

if __name__ == '__main__':
    unittest.main()