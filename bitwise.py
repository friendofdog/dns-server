import sys

byte1 = bytes([80])
# byte1_bin = bin(int.from_bytes(byte1, byteorder=sys.byteorder))
print(bin(ord(byte1)))
# print(ord(byte1))

print('----')

opcode = ''
for bit in range(6, 2, -1):
    # opcode += str(ord(byte1) & (1 << bit))
    opcode += '1' if ord(byte1) & (1 << bit) > 1 else '0'

    # print(ord(byte1) & (1 << bit))
    print(bin(ord(byte1)), bin(1 << bit))
    print(bin(ord(byte1) & (1 << bit)))

print(opcode)
# print(bin(int(opcode)))

# 0001 0000