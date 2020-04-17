import socket


class Server:

    def __init__(self):
        self.port = 53
        self.ip = '127.0.0.1'
        # create a socket using IPV4 (AF_INET) over UDP (SOCK_DGRAM)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start_server(self):
        # bind only takes one param, so have to use tuple
        self.sock.bind((self.ip, self.port))
