'''
In mathematics, the factorial of a non-negative integer n, denoted by n!,
is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120.
By convention the value of 0! is 1.

Write a function to calculate factorial for a given input
'''


#def factorial(n):


n = int(input())
fact = 1
if 0 <= n < 13:
    for i in range(1, n+1):
        fact *= i
    print(fact)
else:
    raise ValueError


def factorial1(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n*factorial1(n-1)
