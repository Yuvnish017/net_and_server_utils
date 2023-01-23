import unittest
from network_utils.src.net_and_server_utils.handling_programs_remotely import XMLRPCClientInterface


class TestHandlingProgramsRemotely(unittest.TestCase):
    def setUp(self) -> None:
        self.HOST = '127.0.0.1'
        self.PORT = 9090

    def test_class_import(self):
        XMLRPCClientInterface()

    def test_client_creation(self):
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.HOST, self.PORT)

    def test_list_of_methods(self):
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.HOST, self.PORT)
        self.assertEqual(len(client.get_methods_server_program()), 4)

    def test_remote_function_response(self):
        client = XMLRPCClientInterface()
        client.create_client_proxy(self.HOST, self.PORT)
        self.assertEqual(client.remote_server_response('add', [2, 3]), 5)


if __name__ == '__main__':
    unittest.main()
