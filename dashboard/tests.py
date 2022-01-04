from dashboard.callAPIs import culltyShorten
import unittest
from unittest.mock import Mock, patch
import json

# Create your tests here.
class shortenPathURL(unittest.TestCase):
    @patch('dashboard.callAPIs.requests.get')
    def test_shorthen_succeeds(self, mock_get):
         resp = Mock(status_code=200)
         resp.json.return_value = {"url" : {"status" : 7, "shortLink" : "this is a test" }}
         mock_get.return_value = resp
        
         url = 'https://www.youtube.com/watch?v=5E_xLmQXOZg'
         short_url = culltyShorten(url)
         print(short_url)
         self.assertNotEqual(short_url, 'Error')
         self.assertEqual(short_url, "this is a test")

    @patch('dashboard.callAPIs.requests.get')
    def test_shorthen_fails_with_wromg_status(self, mock_get):
        resp = Mock(status_code=200)
        resp.json.return_value = {"url" : {"status" : 8, "shortLink" : "this is a test" }}
        mock_get.return_value = resp
        
        url = 'https://www.youtube.com/watch?v=5E_xLmQXOZg'
        short_url = culltyShorten(url)
        print(short_url)
        self.assertEqual(short_url, 'Error')

    @patch('dashboard.callAPIs.requests.get')
    def test_shorthen_fails_with_not_200(self, mock_get):
        resp = Mock(status_code=400)
        mock_get.return_value = resp

        url = 'https://www.youtube.com/watch?v=5E_xLmQXOZg'
        short_url = culltyShorten(url)
        print(short_url)
        self.assertEqual(short_url, 'Server Failed')
