'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24
'''

import re


a = 'foo001'


def increment_string(s):
    number = re.findall(r'\d+', s)
    if number:
        s_number = number[-1]
        s = s.rsplit(s_number, 1)[0]
        number = str(int(s_number) + 1)
        return s + '0' * (len(s_number) - len(number)) + number
    return s + '1'


def increment_string1(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


if a.isalpha():
    a_new = a + '1'
elif a.isdigit():
    a_str = str(int(a) + 1)
    a_new = '0' * (len(a) - len(a_str)) + a_str
else:
    for i in range(len(a)):
        if a[i] not in '0123456789':
            a_1 = a[:i+1]
            a_2 = a[i+1:]
    a_str = str(int(a_2) + 1)
    a_new = a_1 + '0'*(len(a_2) - len(a_str)) + a_str

print(a_new)
