# test_server.py

import unittest
from server import app, messages_lock, messages
import json
import os

class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # Ensure the messages list is empty before each test
        with messages_lock:
            messages.clear()
            if os.path.exists('messages.json'):
                os.remove('messages.json')

    def test_post_message(self):
        response = self.app.post('/messages', json={'text': 'Hello'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['status'], 'Message received')

    def test_get_messages(self):
        self.app.post('/messages', json={'text': 'Hello'})
        response = self.app.get('/messages')
        self.assertEqual(response.status_code, 200)
        messages_data = response.get_json()
        self.assertEqual(len(messages_data), 1)
        self.assertEqual(messages_data[0]['text'], 'Hello')

    def test_get_message_count(self):
        self.app.post('/messages', json={'text': 'Hello'})
        response = self.app.get('/messages/count')
        self.assertEqual(response.status_code, 200)
        count = response.get_json()['count']
        self.assertEqual(count, 1)

if __name__ == '__main__':
    unittest.main()
