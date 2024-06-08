'''
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
'''

def find_it(seq):
    for x in set(seq):
        if seq.count(x) % 2 != 0:
            return x


a = [0, 1, 0, 1, 0]

for i in set(a):
    if a.count(i) % 2 != 0:
        print(i)

print(find_it(a))


