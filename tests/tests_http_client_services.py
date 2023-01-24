import unittest
import io
from unittest import mock
from ..src.net_and_server_utils.http_client_services import HTTPClientServices


class TestHTTPClientServices(unittest.TestCase):
    def setUp(self) -> None:
        self.test_url = 'https://www.python.org/'

    def test_read_url(self):
        http_client = HTTPClientServices(self.test_url)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            http_client.read_url(100)
        self.assertEqual(len(fake_stdout.getvalue().strip()), 100)

    def tearDown(self) -> None:
        del self.test_url
