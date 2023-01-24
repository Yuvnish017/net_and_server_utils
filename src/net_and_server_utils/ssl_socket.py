import ssl
import socket
import pprint


class SSLSocketClient:
    def __init__(self):
        self.context = None
        self.server_hostname = None
        self.port = None
        self.client_instance = None
        self.server_cert = None

    def default_context_creation(self):
        self.context = ssl.create_default_context()

    def manual_context_creation(self, certificates_location):
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.context.load_verify_locations(certificates_location)

    def connect_to_server(self, server_hostname, port_number):
        self.server_hostname = server_hostname
        self.port = port_number
        self.client_instance = self.context.wrap_socket(socket.socket(socket.AF_INET),
                                                        server_hostname=self.server_hostname)
        try:
            self.client_instance.connect((self.server_hostname, self.port))
        except ssl.SSLCertVerificationError:
            print('the server hostname provided does not have ssl certificate')
            print('try another hostname')

    def get_server_certificate(self):
        self.server_cert = self.client_instance.getpeercert()

    def communicate(self):
        while True:
            client_input = input("Enter the data to be transmitted: ")
            if client_input == 'disconnect':
                print("disconnecting from the server...")
                print(" ")
                break
            self.client_instance.sendall(bytes(client_input + '\n', 'utf-8'))
            received_data = str(self.client_instance.recv(1024), 'utf-8')
            print(f"Received data: {received_data}")

    def communicate_and_save(self, filename):
        while True:
            client_input = input("Enter the data to be transmitted: ")
            if client_input == 'disconnect':
                print("disconnecting from the server....")
                print(" ")
                break
            self.client_instance.sendall(bytes(client_input, 'utf-8'))
            received_data = str(self.client_instance.recv(1024), 'utf-8')
            print(f"Received data: {received_data}")
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(received_data + '\n')


class SSLSocketServer:
    def __init__(self):
        self.certificate_file = None
        self.private_key_file = None
        self.hostname = None
        self.port = None
        self.context = None
        self.server_socket = None

    def create_context(self, certificate_file, private_key_file):
        self.certificate_file = certificate_file
        self.private_key_file = private_key_file
        self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.context.load_cert_chain(self.certificate_file, self.private_key_file)

    def bind_and_listen(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.server_socket = socket.socket()
        self.server_socket.bind((self.hostname, self.port))
        self.server_socket.listen(5)

    def accept_and_process_requests(self):
        while True:
            new_socket, from_addr = self.server_socket.accept()
            conn_stream = self.context.wrap_socket(new_socket, server_side=True)
            try:
                data = str(conn_stream.recv(1024), 'utf-8')
                print(f'Received data: {data}')
            finally:
                conn_stream.shutdown(socket.SHUT_RDWR)
                conn_stream.close()
