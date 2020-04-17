def encode_single_byte(*bytes_raw):
    byte_string = ''.join(bytes_raw)
    return int(byte_string, 2).to_bytes(1, byteorder='big')


def encode_int(bytes_raw):
    return int.from_bytes(bytes_raw, byteorder='big')


class ResponseHeader:

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

        r_byte1 = encode_single_byte(qr, opcode, aa, tc, rd)
        r_byte2 = encode_single_byte(ra, z, rcode)
        r_flags = r_byte1 + r_byte2

        self.flags = r_flags

    def build_qdcount(self, q_qdcount):
        # in practice, query count is always 1
        self.qdcount = encode_int(q_qdcount)

    def build_ancount(self, zones, qname, qtype_bytes):
        qtypes = {
            '1': 'A',  # a host address
            '2': 'NS',  # an authoritative name server
            '3': 'MD',  # a mail destination (Obsolete - use MX)
            '4': 'MF',  # a mail forwarder (Obsolete - use MX)
            '5': 'CNAME',  # the canonical name for an alias
            '6': 'SOA',  # marks the start of a zone of authority
            '7': 'MB',  # a mailbox domain name (EXPERIMENTAL)
            '8': 'MG',  # a mail group member (EXPERIMENTAL)
            '9': 'MR',  # a mail rename domain name (EXPERIMENTAL)
            '10': 'NULL',  # a null RR (EXPERIMENTAL)
            '11': 'WKS',  # a well known service description
            '12': 'PTR',  # a domain name pointer
            '13': 'HINFO',  # host information
            '14': 'MINFO',  # mailbox or mail list information
            '15': 'MX',  # mail exchange
            '16': 'TXT',  # text strings
        }

        qtype_int = str(encode_int(qtype_bytes))
        qtype = qtypes[qtype_int].lower()

        try:
            zone = zones[qname]
            self.ancount = len(zone[qtype])
        except KeyError as error:
            raise KeyError(f'No zone file for the domain {error} be be found')

    def build_nscount(self, q_nscount):
        pass

    def build_arcount(self, q_arcount):
        pass
