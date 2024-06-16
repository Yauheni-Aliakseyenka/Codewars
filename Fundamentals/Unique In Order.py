'''
Implement the function unique_in_order which takes as argument a sequence
and returns a list of items without any elements with the same value next to each other
and preserving the original order of elements.
'''


def unique_in_order(sequence):
    if sequence == '' or sequence == '' or sequence == ():
        return []
    new_sequence = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i - 1]:
            new_sequence.append(sequence[i])
    return new_sequence


def unique_in_order1(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


def unique_in_order2(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


def unique_in_order3(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]


def unique_in_order4(iterable):
    return [k for (k, _) in groupby(iterable)] #need from itertools import groupby


a = 'AAAbbbhyyyyA'
b = [1, 2, 2, 3, 3]


