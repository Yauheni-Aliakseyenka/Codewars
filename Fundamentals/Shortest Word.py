'''
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
'''

def find_short(s):
    return min(map(len, s.split()))

def find_short1(s):
    return len(min(s.split(' '), key=len))

s = "bitcoin take over the world maybe who knows perhaps"
