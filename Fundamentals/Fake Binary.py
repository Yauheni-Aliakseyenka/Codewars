'''
Given a string of digits, you should replace any digit below 5 with '0' and
any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
'''


def fake_bin(x):
    new_x = ''
    for i in x:
        if int(i) < 5:
            new_x += '0'
        else:
            new_x += '1'
    return new_x


def fake_bin1(x):
    return ''.join('0' if c < '5' else '1' for c in x)