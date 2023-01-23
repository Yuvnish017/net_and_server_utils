import unittest
from network_utils.src.net_and_server_utils.ssl_socket import SSLSocketClient


class TestSSLSocket(unittest.TestCase):
    def setUp(self) -> None:
        self.server_hostname = 'www.python.org'
        self.port = 443

    def tests_client_class_import(self):
        SSLSocketClient()

    def tests_context_creation(self):
        curr_client = SSLSocketClient()
        curr_client.context_creation()

    def tests_connect_to_server(self):
        curr_client = SSLSocketClient()
        curr_client.context_creation()
        curr_client.connect_to_server(self.server_hostname, self.port)


if __name__ == '__main__':
    unittest.main()
