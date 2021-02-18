# string represents a number in base 2
decimal = int('11001', 2)
print(decimal)

# convert decimal number into a binary. It will prefix the number with 'Ob'
binary = bin(25)
print(binary)

# convert the base 8 to base 10
base_8_to_10 = int('435', 8)
print(base_8_to_10)

# convert the base 7 to base 10
base_7_to_10 = int('10', 7)
print(base_7_to_10)

# convert base 10 to base 16
base_16 = hex(15)
print(base_16)
# hexadecimal to decimal
print(int('b5', 16))
print(int('B5', 16))
print(int('0xb5', 16))

red_hex = hex(213)
green_hex = hex(111)
blue_hex = hex(56)

# convert decimal to octal. '0o' to indicate octal number
print(oct(8))
octal_999 = oct(999)
original = int(octal_999, 8)