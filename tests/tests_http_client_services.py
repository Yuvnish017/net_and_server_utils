import unittest
import io
from urllib.error import HTTPError
from unittest import mock
from ..src.net_and_server_utils.http_client_services import HTTPClientServices


class TestHTTPClientServices(unittest.TestCase):
    def setUp(self) -> None:
        self.test_url = 'https://www.python.org/'
        self.get_url_http_error = 'http://www.musi-cal.com/cgi-bin/query'
        self.get_url = 'https://jsonplaceholder.typicode.com/query'

    def test_read_url(self):
        http_client = HTTPClientServices(self.test_url)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            http_client.read_url(100)
        self.assertEqual(len(fake_stdout.getvalue().strip()), 100)

    def test_get_request_to_url_http_error(self):
        with self.assertRaises(HTTPError):
            http_client = HTTPClientServices(self.get_url_http_error)
            data = {'spam': 1, 'eggs': 2, 'bacon': 3}
            http_client.get_request_to_url(data)

    def test_get_request_to_url_type_error(self):
        with self.assertRaises(TypeError):
            http_client = HTTPClientServices(self.get_url)
            data = ('spam', 'eggs', 'bacon')
            http_client.get_request_to_url(data)

    def tearDown(self) -> None:
        del self.test_url
