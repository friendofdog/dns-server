from io import BytesIO

def readbyte(handle):
    return handle.read(1)

def test_BytesIO():
    b = BytesIO(b'abc')
    assert b'a' == readbyte(b)
    assert b'b' == readbyte(b)
    assert b'c' == readbyte(b)
    assert b''  == readbyte(b)

