'''
The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string, or ")"
if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
'''


def duplicate_encode(word):
    encod_word = ''
    word = word.lower()
    for i in word:
        for y in set(word):
            if i == y and word.count(y) > 1:
                encod_word += '('
            elif i == y and word.count(y) == 1:
                encod_word += ')'
    return encod_word


def duplicate_encode1(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

