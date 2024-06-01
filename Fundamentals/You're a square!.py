'''
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
'''
import sympy
import math

def is_square(n):
    return True if (type(sympy.sqrt(n))) == sympy.core.numbers.Integer else False

def is_square1(n):
    return n>=0 and pow(n, 0.5) % 1 == 0

def is_square2(n):
    return n>=0 and math.sqrt(n).is_integer()




a = float(input())
print(a % 1)