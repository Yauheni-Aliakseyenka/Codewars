'''
Given a string, capitalize the letters that occupy even indexes and odd indexes separately,
and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.
'''


def capitalize(s):
    ev = ''
    for i in range(len(s)):
        if i % 2 == 0:
            ev += s[i].upper()
        else:
            ev += s[i]
    return [ev, ev.swapcase()]


def capitalize1(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]