'''
Given a non-empty array of integers, return the result of multiplying the values together in order.
Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''

def grow(arr):
    pr = 1
    for i in arr:
        pr *= i
    return pr

import math
def grow_1(arr):
    return math.prod(arr)