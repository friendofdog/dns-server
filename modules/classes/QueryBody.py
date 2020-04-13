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
        return f'qname: {self.qname}, qtype: {self.qtype}, qclass: {self.qclass}'
