'''
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
'''


def is_pangram(st):
    count = 0
    for i in set(st.lower()):
        if i.isalpha():
            count += 1
    return count == 26


print(is_pangram('The quick brown fox jumps over the lazy dog.'))


'''a = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XY"
count = 0
for i in set(a.lower()):
    if i.isalpha():
        count += 1

if count == 26:
    print(True)
else:
    print(False)'''

