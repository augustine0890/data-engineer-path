import chardet

# convert character (ASCII) to decimal
decimal = ord('A')
print(bin(decimal))

data = 'CHARACTER'
for c in data:
    print(bin(ord(c)))

# encoding
d = 'data'.encode(encoding='ascii')
print(d)
print(d[0])
print(d[1])
print(d[2])
print(d[3])

v = 'Nê'.encode(encoding='ascii', errors='replace') # throw an error
print(v)
print(type(v))

# create 'bytes' object from hexadecimal
b = bytes.fromhex('ff a9 c8 44 41 54 41')
print(b)
print("length:", len(b))

# Python uses a '\x' to specify that the two characters that follow represent a byte in hexadecimal
# and not ASCII characters
string_1 = 'lowerCase'
string_2 = 'UPPERcASE'
string_3 = 'UPPERCASE'


def check_uppercase(string):
    for c in string:
        if not (ord(c) >= 65 and ord(c) <= 90):
            return False
    return True

print(check_uppercase(string_1))
print(check_uppercase(string_2))
print(check_uppercase(string_3))

# BIG5
trad_chinese = "你好嗎?"
encoded = trad_chinese.encode('BIG5')
print(encoded)
print("length:", len(encoded))

sentence = "ASCII cannot represent these: 你好嗎"
encoded_utf8 = sentence.encode(encoding='utf-8', errors='replace')
print(encoded_utf8)
encoded_ascii = sentence.encode(encoding='ascii', errors='replace')
print(encoded_ascii)

text = "This is encoded - 10£".encode(encoding='utf-8')
print("text: ", text)
# variable named encoded is accessible
decoded_cp1252 = text.decode(encoding='cp1252')
print("cp1252:", decoded_cp1252)
encoding = chardet.detect(text)
print(encoding)
decoded = text.decode(encoding='utf-8')
print(decoded)
