import unittest
from network_utils.src.net_and_server_utils.ssl_socket import SSLSocketClient


class TestSSLSocket(unittest.TestCase):
    def tests_client_class_import(self):
        SSLSocketClient()

    def tests_context_creation(self):
        curr_client = SSLSocketClient()
        curr_client.context_creation()


if __name__ == '__main__':
    unittest.main()
