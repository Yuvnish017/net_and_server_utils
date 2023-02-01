"""
Test Cases for handling_programs_remotely module of net_and_server_utils
"""

import unittest
import sys
sys.path.append('src')
from net_and_server_utils.handling_programs_remotely import XMLRPCClientInterface, XMLRPCServerCreation


def add_list(list_num):
    return sum(list_num)


class TestHandlingProgramsRemotely(unittest.TestCase):
    """
    Test case class
    Assumes that a server is already running in the background
    Change the host address and port accordingly
    """
    def setUp(self) -> None:
        """
        set up fixture for the test cases
        """
        self.host = '127.0.0.1'
        self.port = 9090
        self.server_creation_port = 15000

    def test_client_creation(self):
        """
        tests successful creation of client
        """
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.host, self.port)

    def test_list_of_methods(self):
        """
        tests whether the number of methods on
        server are correctly returned or not
        :return:
        """
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.host, self.port)
        self.assertEqual(len(client.get_methods_server_program()), 4)

    def test_remote_function_response(self):
        """
        tests the response from the server
        """
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.host, self.port)
        self.assertEqual(client.remote_server_response('add', [2, 3]), 5)

    def test_create_server(self):
        server = XMLRPCServerCreation()
        server.create_server(self.host, self.server_creation_port)

    def tests_register_functions(self):
        server = XMLRPCServerCreation()
        server.create_server(self.host, self.server_creation_port)
        server.register_functions([add_list])


if __name__ == '__main__':
    unittest.main()
