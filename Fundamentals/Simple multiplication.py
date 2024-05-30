'''
This kata is about multiplying a given number by eight if it is an even number
and by nine otherwise.
'''
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

def simple_multiplication_1(number):
    return number * 9 if number % 2 else number * 8

def simple_multiplication_2(n):
    return n * (8 + n % 2)