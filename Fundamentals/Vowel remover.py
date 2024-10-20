'''
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
'''


def shortcut(s):
    return ''.join(i for i in s if i not in 'aeiou')


def shortcut1(s):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s


print(shortcut('codewars'))