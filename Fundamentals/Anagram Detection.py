'''
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
Note: anagrams are case insensitive.
Complete the function to return true if the two arguments given are anagrams of each other;
return false otherwise.
'''


def is_anagram(test, original):
    count = 0
    for i in test.lower():
        if i in original.lower() and len(test) == len(original):
            count += 1
    return count == len(original)


def is_anagram1(test, original):
    return sorted(original.lower()) == sorted(test.lower())



