'''
As a part of this Kata, you need to create a function that when provided with a triplet,
returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).
'''


def gimme(input_array):
    x = sorted(input_array)
    return input_array.index(a[1])


def gimme1(input_array):
    return input_array.index(sorted(input_array)[1])


a = [2, 3, 1]


print(sorted(a))