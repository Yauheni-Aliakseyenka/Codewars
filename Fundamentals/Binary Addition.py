'''
Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition.

The binary number returned should be a string.
'''
a = int(input())
b = int(input())

print((bin(a + b)[2::]))

def add_binary(a,b):
    return bin(a + b)[2::]

def add_binary1(a, b):
    return format(a + b, 'b')

print(add_binary(a, b))