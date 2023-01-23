import ssl
import socket


class SSLSocketClient:
    def __init__(self):
        self.context = None

    def context_creation(self):
        self.context = ssl.create_default_context()
