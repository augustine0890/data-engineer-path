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