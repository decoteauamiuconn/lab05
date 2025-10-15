import unittest
from flask import Flask, request
import json
from subscriberserver import app

class MyServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode()), "hello at the root")

    def test_add_subscriber(self):
        response = self.app.post('/add-subscriber', 
                                 data=json.dumps({'name': 'Alice', 'URI': 'http://good.site.com'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('You sent name: Alice and address: http://good.site.com', response.data.decode())

    def test_list_subscribers(self):
        self.app.post('/add-subscriber', 
                      data=json.dumps({'name': 'Alice', 'URI': 'http://good.site.com'}),
                      content_type='application/json')
        response = self.app.get('/list-subscribers')
        self.assertEqual(response.status_code, 200)
        subscribers = json.loads(response.data.decode())
        self.assertIn('Alice', subscribers)
        self.assertEqual(subscribers['Alice'], 'http://good.site.com')
    
    def test_remove_subscriber(self):
        self.app.post('/add-subscriber', 
                      data=json.dumps({'name': 'Alice', 'URI': 'http://good.site.com'}),
                      content_type='application/json')
        response = self.app.post('/remove-subscriber', 
                                 data=json.dumps({'name': 'Alice'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('You removed subscriber: Alice', response.data.decode())
        response = self.app.get('/list-subscribers')
        subscribers = json.loads(response.data.decode())
        self.assertNotIn('Alice', subscribers)

    def test_update_for_subscribers(self):
        self.app.post('/add-subscriber', 
                      data=json.dumps({'name': 'Alice', 'URI': 'http://good.site.com'}),
                      content_type='application/json')
        response = self.app.post('/update-for-subscribers', 
                                 data=json.dumps({'message': 'Hello Subscribers!'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Notified all subscribers with message: Hello Subscribers!', response.data.decode())

    

        

#almost the whole thing autocompleted ? thank you copilot

if __name__ == '__main__':
    unittest.main()

        


