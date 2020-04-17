class QueryHeader:

    def __init__(self, header):
        self.tid = header[:2]
        self.flags = header[2:4]
        self.qdcount = header[4:6]
        self.ancount = header[6:8]
        self.nscount = header[8:10]
        self.arcount = header[10:12]

    def __str__(self):
        return f'tid: {self.tid}, flags: {self.flags}, qdcount: {self.qdcount},' \
               f'ancount: {self.ancount}, nscount: {self.nscount}, arcount: {self.arcount}'
