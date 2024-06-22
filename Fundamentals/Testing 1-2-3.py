'''
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
'''


def number(lines):
    dct = []
    for i in range(len(lines)):
        dct.append(f'{i+1}: {lst[i]}')
    return dct


def number1(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]


a = []
lst = ['a', 'b', 'c']
for i in range(len(lst)):
    a.append(f'{i+1}: {lst[i]}')
print(a)



