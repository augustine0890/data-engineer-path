# Computer Science Concepts
## Binary and Positional Number Systems
- A computer is built with complex electrical circuits. The simplest circuit we can have is a single wire. People build complex electrical circuits that are able to represent sequence of zeros and ones.
- A computer doesn't know the number 0 and 1, but it can distinguish between two states (on/off) of an electrical wire.
- This on/off state of a single wire is called a `bit`.
- With one bit we have two states, with two bits we have four states, with three bits we have eight states and so on. In general, with n bits we have $2^n$ states.
### Decimal System
- The digit at position k has weight $10^k$. The value of a digit is equal to that digit times to its weight.
### Binary System
- Only use the digits `0` and `1` to write the numbers
- The weights of the numbers are powers of 2 rather than powers of 10
### Special Cases
- Base 16 is often called `hexadecimal`
- A group of four bits is called a `nibble`.
- A group of eight bits is called a `byte`. Sequences of eight bits can be used to represent numbers from 0 to 255.
- Hexadecimal is only need two digits to represent a byte
- Example from RGB color system:
    - Colors are represented by three values between 0 and 255 (green, red, blue)
    - One way to represent the color is a tuple (213, 111, 56) or hexadecimal `d56f38`
- A fihe system has three kinds of permissions: read, write, execute

## Encodings and Representing Text
- ASCII is the encoding upon which most encodings are built. It's able to represent a total of 128 characters.
- In the case of textual data: `ASCII encoding`
    - `A` is represented by `65`
    - `B` is represented by `66`
    - `C` is represented by `67`
- ASCII uses 7 bits to represent the characters. The characters are encoded using 8 bits (1 byte) rather than 7 by adding a `0` bit to the left.
- __Unicode__ is not actually an encoding. It is a very big table with 1,114,112 entries that maps symbols to codes.
- All textual data is represented as a sequence of bytes in a computer. In order to read it we need to know which encodings was used.

## Reading and Writing to File
- The `open()` function offers several open modes. Add a `'b'` (which stands for bytes) after the `'r'` or `'w'` in mode. The function will read (or write) it as pure bytes and without trying to decode its contents into a human readable string.
    - `a`: append data to the end of the file
    - `rb`: read the bytes of the file
    - `wb`: write bytes to the file
- A context manager provided a better way to open files as it automatically closes them for us afterwards.
