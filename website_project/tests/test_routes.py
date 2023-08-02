import unittest
from flask import url_for
from website_project.app import create_app
from website_project.models.User import User
from website_project.models.Product import Product
from website_project.models.Order import Order
from website_project.utils.database import db

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        response = self.client.get(url_for('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_product_page(self):
        response = self.client.get(url_for('product', id=1))
        self.assertEqual(response.status_code, 404)

    def test_cart_page(self):
        response = self.client.get(url_for('cart'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_page(self):
        response = self.client.get(url_for('checkout'))
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()