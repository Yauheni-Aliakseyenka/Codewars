'''
Count the number of divisors of a positive integer n.
Random tests go up to n = 500000, but fixed tests go higher.
Note you should only return a number, the count of divisors.
The numbers between parentheses are shown only for you to see which numbers are counted in each case.
'''


def divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


a = 30
count = 0
for i in range(1, a+1):
    if a % i == 0:
        count += 1
print(count)
