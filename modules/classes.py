import socket
import sys


class Server:

    def __init__(self):
        self.port = 53
        self.ip = '127.0.0.1'
        # create a socket using IPV4 (AF_INET) over UDP (SOCK_DGRAM)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start_server(self):
        # bind only takes one param, so have to use tuple
        self.sock.bind((self.ip, self.port))


class Query:

    def __init__(self, server):
        # recvfrom() returns a tuple, allowing data and addr to be set together
        # 512 is the buffer size, which is same as recommended limit for UDP
        self.data, self.addr = server.sock.recvfrom(512)


class ResponseData:

    def __init__(self, data):
        self.tid = data[:2]
        self.flags = data[2:4]


class Response:

    def __init__(self):
        self.tid = ''
        self.qr = ''
        self.opcode = ''
        self.aa = ''

    def __str__(self):
        return f'tid: {self.tid}, qr: {self.qr}, opcode: {self.opcode}, aa: {self.aa}'

    def build_tid(self, tid_raw):
        # the transaction ID is interpreted by Python in an unusable way
        # trim the initial 0x off the start of each byte and return string
        tid = ''
        for byte in tid_raw:
            tid += hex(byte)[2:]

        self.tid = tid

    def build_flags(self, flags_raw):
        byte1 = bytes(flags_raw[:1])
        byte2 = bytes(flags_raw[1:2])

        self.qr = ord(byte1) & (1 << 0)

        opcode = ''
        # for bit in range(1, 5):
        #     opcode += str(ord(byte1) & (1 << bit))

        for bit in range(6, 2, -1):
            opcode += '1' if ord(byte1) & (1 << bit) > 1 else '0'

        self.opcode = opcode

        # self.aa = byte1[5]