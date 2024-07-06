'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.
'''


def al_p(tx):
    return ' '.join(str(ord(x)-96) for x in tx.lower() if x.isalpha())


a = "The sunset sets at twelve o' clock."
'''new_a = ''
for i in a.lower().replace(' ', ''):
    if i.isalpha():
        new_a += str(ord(i)-96) + ' '''''
print(al_p(a))


