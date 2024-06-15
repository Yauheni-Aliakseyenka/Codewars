'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
'''


def accum(st):
    x = 2
    new_st = st[0].upper()
    for i in range(1, len(st)):
        new_st += '-' + (st[i].lower() * x).capitalize()
        x += 1
    return new_st


def accum1(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


print(accum('abcd'))