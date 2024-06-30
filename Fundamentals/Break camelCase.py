'''
Complete the solution so that the function will break up camel casing, using a space between words.
'''


def solution(s):
    new_s = ''
    for i in s:
        if i.islower():
            new_s += i
        else:
            new_s += (' ' + i)
    return new_s


def solution1(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)



