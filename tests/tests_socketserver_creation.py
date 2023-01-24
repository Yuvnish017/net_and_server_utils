"""
Test Cases for socketserver_creation module of net_and_server_utils
"""

import unittest
from network_utils.src.net_and_server_utils.socketserver_creation import TCPServerCreation, UDPServerCreation


class TestSocketServerCreation(unittest.TestCase):
    """
    Test cases class
    """
    def setUp(self) -> None:
        """
        set up fixture for the test cases
        """
        self.HOST = 'localhost'
        self.AVAILABLE_PORT = 8001

    def test_server_creation(self):
        """
        tests successful server creation
        """
        curr_server = TCPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)

    def test_correct_server_address_return(self):
        """
        tests the correctness of server address return
        """
        curr_server = TCPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)
        self.assertEqual(curr_server.get_server_address(), '127.0.0.1')

    def test_correct_port_return(self):
        """
        tests the correctness of port number of the server
        """
        curr_server = TCPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)
        self.assertEqual(curr_server.get_port(), 8001)

    def test_udp_server_creation(self):
        """
        tests successful UDP server creation
        :return:
        """
        curr_server = UDPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)

    def test_correct_udp_server_address_return(self):
        """
        tests the correctness of server address return for UDP server
        """
        curr_server = UDPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)
        self.assertEqual(curr_server.get_server_address(), '127.0.0.1')

    def test_correct_port_return_udp(self):
        """
        tests the correctness of port number return for UDP server
        """
        curr_server = UDPServerCreation()
        curr_server.create_server(self.HOST, self.AVAILABLE_PORT)
        self.assertEqual(curr_server.get_port(), 8001)


if __name__ == '__main__':
    unittest.main()
