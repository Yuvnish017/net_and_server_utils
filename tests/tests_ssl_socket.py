"""
Test cases for ssl_socket module of net_and_server_utils
"""

import ssl
import unittest
import sys
sys.path.append('src')
from net_and_server_utils.ssl_socket import SSLSocketClient, SSLSocketServer


class TestSSLSocket(unittest.TestCase):
    """
    Test cases class
    """
    def setUp(self) -> None:
        """
        set up fixture for the test cases.
        For some cases it is assumed that a server is already running in the background
        Change the server hostnames and ports accordingly prior to running the tests
        """
        # self.server_hostname_with_ssl_certificate = 'www.python.org'
        self.server_hostname_with_ssl_certificate = 'jsonplaceholder.typicode.com'
        self.server_hostname_without_ssl_certificate = 'www.expired.badssl.com'
        self.server_creation_hostaddr = '127.0.0.1'
        self.port = 443
        self.port_server = 12000
        self.response_file = 'socket_server_response.txt'
        self.certificates = "/etc/ssl/certs/ca-bundle.crt"
        self.server_certificate_file = '/Users/yuvnish.malhotra/Desktop/python_training_experiments/certificate.pem'
        self.server_private_key_file = '/Users/yuvnish.malhotra/Desktop/python_training_experiments/key.pem'

    def tests_default_context_creation(self):
        """
        tests the context creation for client
        """
        curr_client = SSLSocketClient()
        curr_client.default_context_creation()

    # def tests_manual_context_creation(self):
    #     """
    #     tests the manual context creation for the client
    #     """
    #     curr_client = SSLSocketClient()
    #     curr_client.manual_context_creation(self.certificates)

    def tests_ssl_cert_verification_error(self):
        """
        tests the raising of SSLCertVerificationError
        """
        with self.assertRaises(ssl.SSLCertVerificationError):
            curr_client = SSLSocketClient()
            curr_client.default_context_creation()
            curr_client.connect_to_server(self.server_hostname_without_ssl_certificate,
                                          self.port)

    def tests_connect_to_server_with_ssl_certificate(self):
        """
        tests successful connection to the server
        """
        curr_client = SSLSocketClient()
        curr_client.default_context_creation()
        curr_client.connect_to_server(self.server_hostname_with_ssl_certificate,
                                      self.port)

    def tests_communicate(self):
        """
        tests whether the data is transferred and received correctly
        """
        curr_client = SSLSocketClient()
        curr_client.default_context_creation()
        curr_client.connect_to_server(self.server_hostname_with_ssl_certificate,
                                      self.port)
        curr_client.communicate()

    def tests_server_creation(self):
        """
        tests the creation of server
        """
        server = SSLSocketServer()
        server.create_context(self.server_certificate_file, self.server_private_key_file)

    def tests_server_binding_and_listening(self):
        """
        tests the binding of server to the hostname and port
        """
        server = SSLSocketServer()
        server.create_context(self.server_certificate_file, self.server_private_key_file)
        server.bind_and_listen(self.server_creation_hostaddr, self.port_server)

    # def tests_server_accepting_requests(self):
    #     """
    #     tests whether the server is processing the requests correctly or not
    #     """
    #     server = SSLSocketServer()
    #     server.create_context(self.server_certificate_file, self.server_private_key_file)
    #     server.bind_and_listen(self.server_hostname_with_ssl_certificate, self.port)
    #     with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    #         server.accept_and_process_requests()
    #     self.assertEqual(list(fake_stdout.getvalue().split('\n'))[0], 'hello')


if __name__ == '__main__':
    unittest.main()
