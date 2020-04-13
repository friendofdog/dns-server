# content of dns-server.py
import pytest
from modules.classes import Zones, QueryHeader, QueryBody, Response

# dig howcode.org @127.0.0.1 +noadflag
header = b'\x88\xd0\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01'
body = b'\x07howcode\x03org\x00\x00\x01\x00\x01\x00\x00)' \
        + b'\x10\x00\x00\x00\x00\x00\x00\x00'
tid = '88d0'
# qr: 0, op: 0000, aa: 0, tc: 0, rd: 1, ra: 0, z: 000, rcode: 0000
flags = b'\x85\x00'
domain = 'howcode.org'

zones = Zones()
query_header = QueryHeader(header)
query_body = QueryBody(body)
response = Response()


def test_zones():
    for zone in zones.zones:
        assert type(zones.zones[zone]) is dict


def test_query_header():
    assert type(header) is bytes
    assert query_header.tid == header[:2]
    assert query_header.flags == header[2:4]
    assert query_header.qdcount == header[4:6]
    assert query_header.ancount == header[6:8]
    assert query_header.nscount == header[8:10]
    assert query_header.arcount == header[10:12]


def test_query_body():
    assert type(query_body.qtype) is bytes
    assert query_body.qtype == b'\x00\x01'
    assert type(query_body.qclass) is bytes
    assert query_body.qclass == b'\x00\x01'
    assert type(query_body.qname) is str
    assert query_body.qname == 'howcode.org'


def test_build_transaction_id():
    q_tid = query_header[:2]
    response.build_tid(q_tid)
    assert type(response.tid) is str
    assert len(response.tid) == 4
    assert response.tid == tid


def test_build_flags():
    q_flags = query_header[2:4]
    response.build_flags(q_flags)
    assert type(response.flags) is bytes
    assert len(response.flags) == 2
    assert response.flags == flags


def test_build_qdcount():
    q_qdcount = query_header[4:6]
    response.build_qdcount(q_qdcount)
    assert type(response.qdcount) is int
    assert response.qdcount == 1
