'''
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
'''
def get_count(sentence):
    return len([i for i in sentence if i in 'aeiou'])

def getCount1(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

def getCount2(s):
    return sum(c in 'aeiou' for c in s)

a = "abracadabra"
print(get_count(a))