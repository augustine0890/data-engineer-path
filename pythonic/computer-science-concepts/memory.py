import sys, os
import numpy as np

x = np.int8(100)
y = np.int8(28)
z = x + y
print(z) # integer overflow

# two's complement bit representation of a number
print(np.binary_repr(127, width=8))

print(np.binary_repr(-2147483648, width=32))
print(np.binary_repr(2147483647, width=32))

# size of object
x = 0
print("0:", sys.getsizeof(x))

x = 9223372036854775807 # maximum value for 64-bit integers
print(sys.getsizeof(x))

# bytes required to represent 32-bit integers
num_bytes = sys.getsizeof(2147483647)
num_mb = round(num_bytes*1000000000/1000000) # 1 billion integers
print(num_mb)

# bits required to represent a given integer
print(int.bit_length(12))

def minimum_required_bits(list_of_integers):
    min_req_bits = 0
    for value in list_of_integers:
        nb_bits = int.bit_length(value)
        min_req_bits = max(min_req_bits, nb_bits)
    return min_req_bits

print(minimum_required_bits([23, 43, -22]))

# 1 billion integers fit into 32-bit
with open('identifiers.txt', encoding='utf8') as file:
    values = [int(value) for value in list(file)]
    print(minimum_required_bits(values))

# size in bytes
print(sys.getsizeof(""))
print(sys.getsizeof("data"))

s = "你"
size_s = sys.getsizeof(s)
print(size_s)
size_ss = sys.getsizeof(s + s)
print(size_ss)

# 66 = 49 + 1 * 17 [49 (overhead) + 17 (1 byte per character)]
print("latin-1", sys.getsizeof("Learning Python !"))  

# 108 = 74 + 2 * 17 [74 (overhead) + 17 * 2 (2 bytes per character)]
print("ucs-2", sys.getsizeof("Learning Python 吧")) # UCS-2 encoding

# 144 = 76 + 4 * 17 [76 (overhead) + 17 * 4 (4 bytes per character)]
print("ucs-4", sys.getsizeof("Learning Python 🐍")) # UCS-4 encoding

message = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"
message_latin_bytes = message.encode(encoding='Latin-1', errors='ignore')
cleaned_message = message_latin_bytes.decode(encoding='Latin-1')
message_size = sys.getsizeof(message)
cleaned_message_size = sys.getsizeof(cleaned_message)

with open('utf8.txt', 'w', encoding='utf8') as file:
    file.write(message)
size_utf8 = os.path.getsize('utf8.txt')
print("size_utf8", size_utf8)

with open('utf32.txt', 'w', encoding='utf32') as file:
    file.write(message)
size_utf32 = os.path.getsize('utf32.txt')
print("size_utf32", size_utf32)

# How much disk space will be required to store all transactions in website for next 20 years
num_days_in_a_year = 365
num_years = 20
bytes_per_char = 32 / 8
num_transactions = 1000000
username_size = 20
product_name_size = 50

day_gb = (2*bytes_per_char*username_size + bytes_per_char*product_name_size)*num_transactions/(10**9)
num_gb = day_gb * num_days_in_a_year * num_years