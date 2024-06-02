'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers
and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
'''

def count_positives_sum_negatives(arr):
    a = [0, 0]
    if arr == []:
        a = arr
    for i in arr:
        if i > 0:
            a[0] += 1
        else:
            a[1] += i
    return a

def count_positives_sum_negatives1(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

test = []

print(count_positives_sum_negatives(test))