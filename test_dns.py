# content of dns-server.py
import pytest
from modules.classes import Server, Query, Response

# dig howcode.org @127.0.0.1 +noadflag
query = b'\x88\xd0\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01' \
        + b'\x07howcode\x03org\x00\x00\x01\x00\x01\x00\x00)' \
        + b'\x10\x00\x00\x00\x00\x00\x00\x00'

tid = '88d0'

# qr = 0, op = 0000, aa=0, tc = 0, rd = 1, ra = 0, z = 000, rcode = 0000
flags = b'\x85\x00'


def test_build_transaction_id():
    q_tid = query[:2]
    r = Response()
    r.build_tid(q_tid)
    assert type(r.tid) is str
    assert len(r.tid) == 4
    assert r.tid == tid


def test_build_flags():
    q_flags = query[2:4]
    r = Response()
    r.build_flags(q_flags)
    assert type(r.flags) is bytes
    assert len(r.flags) == 2
    assert r.flags == flags
