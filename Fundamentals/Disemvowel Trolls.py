'''
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata 'y' isn't considered a vowel.
'''
def disemvowel(string_):
    new_string = ''
    for i in string_:
        if i.lower() not in 'euioa':
           new_string += i
    return new_string

def disemvowel_1(string_):
    for i in string_:
        if i.lower() in 'euioa':
           string_ = string_.replace(i, '')
    return string_

def disemvowel_2(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

n = input()
print(disemvowel_1(n))
