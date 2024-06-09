'''
Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length
and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
'''

def is_triangle(a, b, c):
    return c < a + b and a < c + b and b < a + c


def is_triangle1(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c


a, b, c = map(int, input().split())

print(is_triangle(a, b, c))


