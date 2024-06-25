'''
We need a function to collect these numbers, that may receive two integers a, b that defines the range
[a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

If there are no numbers of this kind in the range [a,b] the function should output an empty list.
'''


def sum_dig_pow(a, b):
    new_arr = []
    for i in range(a, b + 1):
        num = 0
        for x, y in enumerate(str(i)):
            num += int(y) ** (x + 1)
        if num == i:
            new_arr.append(i)
    return new_arr


def sum_dig_pow1(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]


def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))


def sum_dig_pow2(a, b):
    return [x for x in range(a,b + 1) if x == dig_pow(x)]


print(sum_dig_pow(89, 135))



