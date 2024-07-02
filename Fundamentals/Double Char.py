'''
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
'''


def double_char(s):
    return ''.join(2*i for i in s)


print(double_char("String"))