# content of dns.py
import pytest
from modules.classes import Server, Query, Response


def test_build_transaction_id():
    raw_tid = b'\xbb\xa6\x01 \x00\x01\x00\x00\x00\x00\x00\x01' \
        + b'\x07howcode\x03org\x00\x00\x01\x00\x01\x00\x00)' \
        + b'\x10\x00\x00\x00\x00\x00\x00\x00'
    r = Response()
    r.build_tid(raw_tid)
    #assert 'XXX' == r.tid
