'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:

Sam Harris => S.H

patrick feeney => P.F
'''
def abbrev_name(name):
    name = name.title().split()
    return (f'{name[0][0]}.{name[1][0]}')

def abbrevName1(name):
    return '.'.join(w[0] for w in name.split()).upper()

def abbrevName2(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

s = 'sam harris'
s1 = 'sam harris'
s = s.title().split()
print(f'{s[0][0]}.{s[1][0]}')
print(abbrev_name(s1))