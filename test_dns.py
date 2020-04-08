# content of dns.py
import pytest
from modules.classes import Server, Query, Response

class TestResponse:

    def test_build_transaction_id(self, data = b'\xbb\xa6\x01 \x00\x01\x00\x00\x00\x00\x00\x01\x07howcode\x03org\x00\x00\x01\x00\x01\x00\x00)\x10\x00\x00\x00\x00\x00\x00\x00'):
        assert type(data) is bytes
        assert data[:2]
