'''
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of
the sequence to generate the next. And, worse part of it,
regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1]
as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
'''


def tribonacci(signature, n):
    new_arr = []
    for i in range(n):
        if len(new_arr) < 3:
            new_arr.append(signature[i])
        else:
            new_arr.append(sum(new_arr[-1:-4:-1]))
    return new_arr


def tribonacci1(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res

'''a = [1, 1, 1]
b = 8

x = [sum(a)]
a += x
print(x)
#y = a + x
print(a)
while b - len(a) != 0:
    a.append(sum(a[-1:-4:-1]))
print(a)'''


