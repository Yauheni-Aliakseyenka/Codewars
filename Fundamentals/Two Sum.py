'''
Write a function that takes an array of numbers (integers for the tests) and a target number.
It should find two different items in the array that, when added together, give the target value.
The indices of these items should then be returned in a tuple / list (depending on your language)
like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater,
and all of the items will be numbers; target will always be the sum of two different items from that array).
'''


a = [1234, 5678, 9012]
b = 14690
x = []

for j in range(len(a)):
    for i in range(j+1, len(a)):
        if a[j] + a[i] == b:
            x.append(j)
            x.append(i)
        break
    if sum(x):
        break

def two_sum1(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]


print(tuple(x))


