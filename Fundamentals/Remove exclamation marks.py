'''
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
'''


def remove_exclamation_marks(s):
    return ''.join(i for i in s if i != '!')


def remove_exclamation_marks1(s):
    return s.replace('!', '')