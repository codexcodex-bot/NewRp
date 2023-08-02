import unittest
from website_project.models.User import User
from website_project.models.Product import Product
from website_project.models.Order import Order
from website_project.utils.database import db

class TestModels(unittest.TestCase):

    def setUp(self):
        self.user = User('testuser', 'testpassword', 'testemail@test.com')
        self.product = Product('testproduct', 'testdescription', 10.0, 'testimage.jpg')
        self.order = Order(self.user.id, self.product.id, 1)

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, 'testpassword')
        self.assertEqual(self.user.email, 'testemail@test.com')

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'testproduct')
        self.assertEqual(self.product.description, 'testdescription')
        self.assertEqual(self.product.price, 10.0)
        self.assertEqual(self.product.image, 'testimage.jpg')

    def test_order_creation(self):
        self.assertEqual(self.order.user_id, self.user.id)
        self.assertEqual(self.order.product_id, self.product.id)
        self.assertEqual(self.order.quantity, 1)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()