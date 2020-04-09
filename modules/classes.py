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


class Query:

    def __init__(self, server):
        # recvfrom() returns a tuple, allowing data and addr to be set together
        # 512 is the buffer size, which is same as recommended limit for UDP
        self.data, self.addr = server.sock.recvfrom(512)


class ResponseData:

    def __init__(self, data):
        self.tid = data[:2]
        self.flags = data[2:4]
        self.qdcount = data[4:5]
        self.ancount = data[5:6]
        self.nscount = data[6:7]
        self.arcount = data[7:8]


def encode_bytes(*bytes_raw):
    byte_string = ''.join(bytes_raw)
    return int(byte_string, 2).to_bytes(1, byteorder='big')


class Response:

    def __init__(self):
        self.tid = ''
        self.flags = ''
        self.qdcount = ''
        self.ancount = ''
        self.nscount = ''
        self.arcount = ''

    def __str__(self):
        return f'tid: {self.tid}, flags: {self.flags}, qdcount: {self.qdcount}, ' \
               f'ancount: {self.ancount}, nscount: {self.nscount}, arcount: {self.arcount}'

    def build_tid(self, q_tid):
        # response sends back same ID as query
        self.tid = q_tid.hex()

    def build_flags(self, q_flags):
        q_byte1 = bytes(q_flags[:1])
        # not currently using byte 2 of flags, so comment out for now
        # q_byte2 = bytes(q_flags[1:2])

        # sending response, so value is 1
        qr = '1'

        opcode = ''

        # below suggested by HowCode, but does not operate on correct bytes
        # for bit in range(1, 5):
        #     opcode += str(ord(byte1) & (1 << bit))

        # below operates on bits 1~4
        for bit in range(6, 2, -1):
            opcode += '1' if ord(q_byte1) & (1 << bit) > 1 else '0'

        # assume that server is giving authoritative answer
        # this could be expanded later to check authoritativeness
        aa = '1'

        # assume that response is short and therefore not truncated
        tc = '0'

        # was to 0 in HowCode, but it should be set by query
        rd = str(ord(q_byte1) & (1 << 0))

        # recursion is not available
        ra = '0'

        # must be 0
        z = '000'

        # assume there are no errors and return 0
        # this could be expanded later to check and return errors
        rcode = '0000'

        r_byte1 = encode_bytes(qr, opcode, aa, tc, rd)
        r_byte2 = encode_bytes(ra + z + rcode)
        r_flags = r_byte1 + r_byte2

        self.flags = r_flags

    def build_qdcount(self, q_qdcount):
        pass

    def build_ancount(self, q_ancount):
        pass

    def build_nscount(self, q_nscount):
        pass

    def build_arcount(self, q_arcount):
        pass
