# content of dns-server.py
import pytest
from dns import *
from dns.responseheader import encode_single_byte, encode_int

# dig howcode.org @127.0.0.1 +noadflag
header = b'\x88\xd0\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01'
body = b'\x07howcode\x03org\x00\x00\x01\x00\x01\x00\x00)' \
        + b'\x10\x00\x00\x00\x00\x00\x00\x00'
tid = '88d0'
flag_byte1 = ('1', '0000', '1', '0', '1')
flag1 = b'\x85'
flags = b'\x85\x00'
qname = 'howcode.org.'
qtype_bytes = b'\x00\x01'
qclass_bytes = b'\x00\x01'

zones = Zones()
query_header = QueryHeader(header)
query_body = QueryBody(body)
response = ResponseHeader()


def test_zones():
    for zone in zones.zones:
        assert type(zones.zones[zone]) is dict


def test_query_header():
    header = b'\x88\xd0\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01'
    qh = QueryHeader(header)
    assert 'flags' in str(qh)

def test_query_body():
    assert type(query_body.qtype) is bytes
    assert query_body.qtype == qtype_bytes
    assert type(query_body.qclass) is bytes
    assert query_body.qclass == qclass_bytes
    assert type(query_body.qname) is str
    assert query_body.qname == qname


def test_build_transaction_id():
    response.build_tid(query_header.tid)
    assert type(response.tid) is str
    assert len(response.tid) == 4
    assert response.tid == tid


def test_build_flags():
    response.build_flags(query_header.flags)
    assert type(response.flags) is bytes
    assert len(response.flags) == 2
    assert response.flags == flags


def test_build_qdcount():
    response.build_qdcount(query_header.qdcount)
    assert type(response.qdcount) is int
    assert response.qdcount == 1


def test_build_ancount():
    response.build_ancount(zones.zones, qname, qtype_bytes)
    assert type(response.ancount) is int
    assert response.ancount == 5


def test_encode_single_byte():
    encoded = encode_single_byte(*flag_byte1)
    assert len(encoded) == 1
    assert type(encoded) is bytes
    assert encoded == flag1


def test_encode_int():
    inted = encode_int(qtype_bytes)
    assert type(inted) is int
    assert inted == 1
