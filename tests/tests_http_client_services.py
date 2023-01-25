"""
Test cases for http_client_services module of net_and_server_utils
"""

import unittest
import io
from urllib.error import HTTPError
from unittest import mock
import sys
sys.path.append('../')
from network_utils.src.net_and_server_utils.http_client_services import HTTPClientServices


class TestHTTPClientServices(unittest.TestCase):
    """
    unit test class
    """
    def setUp(self) -> None:
        """
        set up fixture for test cases
        """
        self.test_url = 'https://www.python.org/'
        self.url_http_error = 'http://www.musi-cal.com/cgi-bin/query'
        self.get_url = 'https://jsonplaceholder.typicode.com/'

    def test_read_url(self):
        """
        tests the read_url method
        Whether it prints the correct amount of data or not
        """
        http_client = HTTPClientServices(self.test_url)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            http_client.read_url(100)
        self.assertEqual(len(fake_stdout.getvalue().strip()), 100)

    def test_get_request_to_url_http_error(self):
        """
        tests the get_request_to_url for http error
        """
        with self.assertRaises(HTTPError):
            http_client = HTTPClientServices(self.url_http_error)
            data = {'spam': 1, 'eggs': 2, 'bacon': 3}
            http_client.get_request_to_url(data)

    def test_get_request_to_url_type_error(self):
        """
        tests the get_request_to_url for type error
        TypeError occurs when data passed is on the wrong format
        """
        with self.assertRaises(TypeError):
            http_client = HTTPClientServices(self.get_url)
            data = ('spam', 'eggs', 'bacon')
            http_client.get_request_to_url(data)

    def test_post_request_to_url_http_error(self):
        """
        tests the post_request_to_url method for http error
        """
        with self.assertRaises(HTTPError):
            http_client = HTTPClientServices(self.url_http_error)
            data = {'spam': 1, 'eggs': 2, 'bacon': 3}
            http_client.post_request_to_url(data)

    def test_post_request_to_url_type_error(self):
        """
        tests the post_request_to_url method for type error
        TypeError occurs when the data passed is in wrong format
        """
        with self.assertRaises(TypeError):
            http_client = HTTPClientServices(self.get_url)
            data = ('spam', 'eggs', 'bacon')
            http_client.post_request_to_url(data)

    def tearDown(self) -> None:
        """
        tear down fixture for the test cases
        """
        del self.test_url
        del self.url_http_error
        del self.get_url


if __name__ == '__main__':
    unittest.main()
