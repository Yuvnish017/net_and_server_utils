import ssl
import socket


class SSLSocketClient:
    def __init__(self):
        self.context = None
        self.server_hostname = None
        self.port = None
        self.client_instance = None

    def context_creation(self):
        self.context = ssl.create_default_context()

    def connect_to_server(self, server_hostname, port_number):
        self.server_hostname = server_hostname
        self.port = port_number
        self.client_instance = self.context.wrap_socket(socket.socket(socket.AF_INET),
                                                        server_hostname=self.server_hostname)
        self.client_instance.connect((self.server_hostname, self.port))
