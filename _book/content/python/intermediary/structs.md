# Converts any type (string, number, boolean, etc...) to byte format

from struct import *

# Stores as byte data
# pack(type_of_data, values)
packed_data = pack('iif', 6, 19, 4.73)  # Convert two intergers and a float 'iif' to byte data
print(packed_data)  # b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'

print(calcsize('i'))  # 4 bytes | Size needed to store an integer
print(calcsize('f'))  # 4 bytes | size needed to store a float
print(calcsize('iif'))  # 12 bytes | size needed to store two integers plus and a float

# Get bytes data back to normal
original_data = unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')

print(original_data)
