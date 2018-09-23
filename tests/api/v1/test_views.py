import unittest
from app import create_app

from app.api.v1.views import orders, Order_list

class TestStrings(unittest.TestCase):
    def test_returns_orders(self):
        self.assertEqual(get())

if __name__ == '__main__':
       unittest.main()
