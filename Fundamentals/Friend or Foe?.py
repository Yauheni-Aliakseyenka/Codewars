'''
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
Note: keep the original order of the names in the output.
'''
from typing import List


def friend(x):
    new_list = []
    for i in x:
        if len(i) == 4:
            new_list.append(i)
    return new_list


def friend1(x):
    return [f for f in x if len(f) == 4]


def friend2(x):
    return filter(lambda name: len(name) == 4, x)


a = ["Ryan", "Jimmy", "abc", "d", "Cool Man"]


print(friend(a))