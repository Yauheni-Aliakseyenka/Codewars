'''
Build a function that returns an array of integers from n to 1 where n>0.
'''


def reverse_seq(n):
    return [i for i in range(n, 0, -1)]


def reverse_seq1(n):
    return list(range(n, 0, -1))


print(reverse_seq(5))