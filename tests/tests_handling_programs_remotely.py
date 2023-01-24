"""
Test Cases for handling_programs_remotely module of net_and_server_utils
"""

import unittest
from network_utils.src.net_and_server_utils.handling_programs_remotely import XMLRPCClientInterface


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
        self.HOST = '127.0.0.1'
        self.PORT = 9090

    def test_client_creation(self):
        """
        tests successful creation of client
        """
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.HOST, self.PORT)

    def test_list_of_methods(self):
        """
        tests whether the number of methods on
        server are correctly returned or not
        :return:
        """
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.HOST, self.PORT)
        self.assertEqual(len(client.get_methods_server_program()), 4)

    def test_remote_function_response(self):
        """
        tests the response from the server
        """
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.HOST, self.PORT)
        self.assertEqual(client.remote_server_response('add', [2, 3]), 5)


if __name__ == '__main__':
    unittest.main()
