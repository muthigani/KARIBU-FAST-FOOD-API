import unittest
from flask import json,jsonify,request
from views import app, Order, Order_list
from base64 import b64encode

class EndpointTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        
    
    
    def test_to_get_all_orders(self):
        response = self.app.get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)

    """These tests check  status codes """    

    def test_to_fetch_aspecific_order(self):
        response = self.app.get('/api/v1/orders/2')
        self.assertEqual(response.status_code,200)

    def test_to_throw_type_error_when_string_ispassed_as_id(self):
        order_id = "1"
        api_url = '/api/v1/ordersss/'+ order_id
        response = self.app.get(api_url)
        self.assertRaises(TypeError, response)

    def test_to_fetch_order_when_string_ispassed_as_id(self):
        order_id = "1"
        api_url = '/api/v1/orders/'+ order_id
        response = self.app.get(api_url)
        self.assertEqual(response.status_code, 200)

    def test_to_fetch_specific_order_when_nonexistant_is_ispassed(self):
        response = self.app.get('/api/v1/orders/9')
        self.assertEqual(response.status_code,200)
   
    
    """This test function checks if mandatory parameter food is not passed"""
    def test_for_mandatory_parameter_missing_in_placed_order(self):
        response = self.app.post('/api/v1/orders',data = json.dumps({"Description": "Tasty food"}), 
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,405)

    """This test function check whether food  parameter is a string"""
    def test_to_throw_type_error_when_str_is_notpassed_as_parameter(self):
        response = self.app.post('/api/v1/orders',data = json.dumps({"food": 4}), 
                                content_type="application/json", follow_redirects=True)
        self.assertRaises(TypeError, response)

def tearDown(self):
        pass
   


if __name__ == "__main__":
    unittest.main()