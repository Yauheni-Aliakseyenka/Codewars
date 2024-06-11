'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
'''


def find_uniq(arr):
    for i in range(len(arr)):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1-len(arr)]:
            uniq = arr[i]
            break
    return uniq


def find_uniq1(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


a = [3, 3, 3, 3, 3, 10]

print(find_uniq(a))
