import unittest
from network_utils.src.net_and_server_utils.socketserver_creation import TCPServerCreation, UDPServerCreation


class TestSocketServerCreation(unittest.TestCase):
    def setUp(self) -> None:
        self.HOST = 'localhost'
        self.AVAILABLE_PORT = 8001

    def test_tcp_class_run(self):
        TCPServerCreation()

    def test_server_creation(self):
        curr_server = TCPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)

    def test_correct_server_address_return(self):
        curr_server = TCPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)
        self.assertEqual(curr_server.get_server_address(), '127.0.0.1')

    def test_correct_port_return(self):
        curr_server = TCPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)
        self.assertEqual(curr_server.get_port(), 8001)

    def test_udp_class_run(self):
        UDPServerCreation()

    def test_udp_server_creation(self):
        curr_server = UDPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)

    def test_correct_udp_server_address_return(self):
        curr_server = UDPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)
        self.assertEqual(curr_server.get_server_address(), '127.0.0.1')

    def test_correct_port_return_udp(self):
        curr_server = UDPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)
        self.assertEqual(curr_server.get_port(), 8001)


if __name__ == '__main__':
    unittest.main()
