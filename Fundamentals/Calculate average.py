'''
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
'''

def find_average(numbers):
    if numbers:
        return sum(numbers)/len(numbers)
    else:
        return 0

def find_aver_new(array):
    return sum(array) / len(array) if array else 0

a = []
print(find_average(a))