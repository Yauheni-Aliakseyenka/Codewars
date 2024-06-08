'''
Create a function with two arguments that will return an array of the first n multiples of x.
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array or list ( depending on language ).
'''

def count_by(x, n):
    a =[]
    for i in range(1, n+1):
        a.append(x * i)
    return a

def count_by1(x, n):
    return [i * x for i in range(1, n + 1)]


print(count_by(3, 5))