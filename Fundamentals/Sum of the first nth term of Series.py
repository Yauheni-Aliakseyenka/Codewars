'''
Your task is to write a function which returns the n-th term of the following series,
which is the sum of the first n terms of the sequence (n is the input parameter).

You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return "0.00".

You will only be given Natural Numbers as arguments.
'''


def series_sum(n):
    return '{:.2f}'.format(sum(1/(i*3 + 1) for i in range(n)))


print(series_sum(0))
'''n = int(input())
num = 0
for i in range(n):
    num += 1/(i*3 + 1)

print("{:.2f}".format(num))'''