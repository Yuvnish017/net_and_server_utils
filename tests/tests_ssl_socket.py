import ssl
import unittest
from network_utils.src.net_and_server_utils.ssl_socket import SSLSocketClient, SSLSocketServer
from unittest import mock
import io


class TestSSLSocket(unittest.TestCase):
    def setUp(self) -> None:
        self.server_hostname_with_ssl_certificate = '127.0.0.1'
        self.server_hostname_without_ssl_certificate = 'www.expired.badssl.com'
        self.port = 11000
        self.port_server = 12000
        self.response_file = 'socket_server_response.txt'
        self.certificates = "/etc/ssl/certs/ca-bundle.crt"
        self.server_certificate_file = '/Users/yuvnish.malhotra/Desktop/python_training_experiments/certificate.pem'
        self.server_private_key_file = '/Users/yuvnish.malhotra/Desktop/python_training_experiments/key.pem'

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
        curr_client.manual_context_creation(self.server_certificate_file)
        curr_client.connect_to_server(self.server_hostname_with_ssl_certificate,
                                      self.port)

    def tests_communicate_and_save(self):
        curr_client = SSLSocketClient()
        curr_client.default_context_creation()
        # curr_client.manual_context_creation(self.server_certificate_file)
        curr_client.connect_to_server(self.server_hostname_with_ssl_certificate,
                                      self.port)
        curr_client.communicate_and_save(self.response_file)
        count = 0
        with open(self.response_file, 'r') as file:
            for _ in file:
                count += 1
        self.assertEqual(count, 1)

    def tests_server_creation(self):
        server = SSLSocketServer()
        server.create_context(self.server_certificate_file, self.server_private_key_file)

    def tests_server_binding_and_listening(self):
        server = SSLSocketServer()
        server.create_context(self.server_certificate_file, self.server_private_key_file)
        server.bind_and_listen(self.server_hostname_with_ssl_certificate, self.port)

    def tests_server_accepting_requests(self):
        server = SSLSocketServer()
        server.create_context(self.server_certificate_file, self.server_private_key_file)
        server.bind_and_listen(self.server_hostname_with_ssl_certificate, self.port)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            server.accept_and_process_requests()
        self.assertEqual(list(fake_stdout.getvalue().split('\n'))[0], 'hello')


if __name__ == '__main__':
    unittest.main()
