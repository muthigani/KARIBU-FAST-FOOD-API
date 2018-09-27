import unittest
from flask import Flask,json,jsonify,request

app = Flask(__name__)



class EndpointTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        
    
    
    def test_to_get_all_orders(self):
        """These tests check  status codes """ 
        response = self.app.get('/api/v1/orders')
        self.assertTrue(response.status_code, 200)

       

    def test_to_fetch_specific_order(self):
        """These tests check  status codes """ 
        response = self.app.get('/api/v1/orders/2')
        self.assertTrue(response.status_code, 200)

    def test_error_id(self):
        """These tests check  status codes """ 
        order_id = "1"
        api_url = '/api/v1/ordersss/'+ order_id
        response = self.app.get(api_url)
        self.assertRaises(TypeError, response)

    def test_to_fetch_order_id(self):
        """These tests check  status codes """
        order_id = "1"
        api_url = '/api/v1/orders/'+ order_id
        response = self.app.get(api_url)
        self.assertTrue(response.status_code, 200)

    def test_to_fetch_specific_order_when_nonexistant_is_ispassed(self):
        """These tests check  status codes """
        response = self.app.get('/api/v1/orders/9')
        self.assertEqual(response.status_code,404)
   
    

    def test_for_mandatory_parameter_missing_in_placed_order(self):
        """Test to checks if mandatory parameter food is not passed"""
        response = self.app.post('/api/v1/orders',data = json.dumps({"Description": "Tasty food"}), 
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,404)

    
    def test_error_when_str_is_notpassed_as_parameter(self):
        """Test to check whether food  parameter is a string"""
        response = self.app.post('/api/v1/orders',data = json.dumps({"food": 7}), 
                                content_type="application/json", follow_redirects=True)
        self.assertRaises(TypeError, response)

def tearDown(self):
        pass
   


if __name__ == "__main__":
    unittest.main()