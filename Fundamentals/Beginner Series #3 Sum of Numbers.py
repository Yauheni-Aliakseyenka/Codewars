'''
Given two integers a and b, which can be positive or negative, find the sum of all the integers between
and including them and return it. If the two numbers are equal return a or b.
'''


def get_sum(a,b):
    return sum(i for i in range(min(a,b), max(a,b)+1))


def get_sum1(a,b):
    return sum(range(min(a, b), max(a, b) + 1))


print(get_sum(1, 0))