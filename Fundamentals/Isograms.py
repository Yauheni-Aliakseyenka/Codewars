'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
'''

def is_isogram(string):
    for i in string.lower():
        if string.lower().count(i) != 1:
            return False
            break
    return True

def is_isogram1(string):
    return len(string) == len(set(string.lower()))


n = input()
print(is_isogram(n))


