'''
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
'''
import re


def replace_exclamation(st):
    new_st = ''
    for i in st:
        if i in 'aeyuioAEYUIO':
            i = '!'
        new_st += i
    return new_st


def replace_exclamation1(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


def replace_exclamation2(s):
    return re.sub('[aeiouAEIOU]', '!', s)


print(replace_exclamation('ABCDE'))
