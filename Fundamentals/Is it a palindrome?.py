'''
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.
'''


def is_palindrome(s):
    return s.lower() == s[::-1].lower()


print(is_palindrome('aba'))
