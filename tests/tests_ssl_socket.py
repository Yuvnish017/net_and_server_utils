import ssl
import unittest
from network_utils.src.net_and_server_utils.ssl_socket import SSLSocketClient


class TestSSLSocket(unittest.TestCase):
    def setUp(self) -> None:
        self.server_hostname_with_ssl_certificate = 'www.python.org'
        self.server_hostname_without_ssl_certificate = 'www.expired.badssl.com'
        self.port = 443
        self.response_file = 'socket_server_response.txt'
        self.certificates = "/etc/ssl/certs/ca-bundle.crt"

    def tests_client_class_import(self):
        SSLSocketClient()

    def tests_default_context_creation(self):
        curr_client = SSLSocketClient()
        curr_client.default_context_creation()

    def tests_manual_context_creation(self):
        curr_client = SSLSocketClient()
        curr_client.manual_context_creation(self.certificates)

    def tests_ssl_cert_verification_error(self):
        with self.assertRaises(ssl.SSLCertVerificationError):
            curr_client = SSLSocketClient()
            curr_client.default_context_creation()
            curr_client.connect_to_server(self.server_hostname_without_ssl_certificate,
                                          self.port)

    def tests_connect_to_server_with_ssl_certificate(self):
        curr_client = SSLSocketClient()
        curr_client.default_context_creation()
        curr_client.connect_to_server(self.server_hostname_with_ssl_certificate,
                                      self.port)

    def tests_communicate_and_save(self):
        curr_client = SSLSocketClient()
        curr_client.default_context_creation()
        curr_client.connect_to_server(self.server_hostname_with_ssl_certificate,
                                      self.port)
        curr_client.communicate_and_save(self.response_file)
        count = 0
        with open(self.response_file, 'r') as file:
            for _ in file:
                count += 1
        self.assertEqual(count, 1)


if __name__ == '__main__':
    unittest.main()
