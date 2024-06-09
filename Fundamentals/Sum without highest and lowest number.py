'''
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element
( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge,
even if there are more than one with the same value.

Mind the input validation.
'''

def sum_array(arr):
    if arr == None or arr == []:
        return 0
    arr.sort()
    return sum(arr[1:len(arr)-1])


def sum_array1(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


def sum_array2(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


a = [6, 2, 1, 8, 10]


print(sum_array(a))
