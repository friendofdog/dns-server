class Query:

    def __init__(self, server):
        # recvfrom() returns a tuple, allowing data and addr to be set together
        # 512 is the buffer size, which is same as recommended limit for UDP
        self.data, self.addr = server.sock.recvfrom(512)

def parse_body(qname):
    qname_parts = []

    while len(qname) > 0:
        length = qname[0]
        part = qname[1:length + 1]
        qname_parts.append(part.decode('utf-8'))
        qname = qname.split(part)[1]

    return '.'.join(qname_parts) + '.'


class QueryBody:

    def __init__(self, body):
        qname_bytes = body.split(b'\x00')[0]

        self.qtype = body.split(qname_bytes)[1][1:3]
        self.qclass = body.split(qname_bytes)[1][3:5]
        self.qname = parse_body(qname_bytes)

    def __str__(self):
        return \
            f'qname: {self.qname}, qtype: {self.qtype}, qclass: {self.qclass}'

class QueryHeader:

    def __init__(self, header):
        self.tid = header[:2]
        #self.flags = header[2:4]
        self.qdcount = header[4:6]
        self.ancount = header[6:8]
        self.nscount = header[8:10]
        self.arcount = header[10:12]

    def __str__(self):
        return \
            f'tid: {self.tid}, qdcount: {self.qdcount},' \
            f'ancount: {self.ancount}, nscount: {self.nscount}, ' \
            f'arcount: {self.arcount}'
