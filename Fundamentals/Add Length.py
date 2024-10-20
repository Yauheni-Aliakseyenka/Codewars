'''
What if we need the length of the words separated
by a space to be added at the end of that same word and have it returned as an array?

Your task is to write a function that takes a String and returns an Array/list
with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.
'''


def add_length(str_):
    return [i + ' ' + str(len(i)) for i in str_.split()]


def add_length1(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]


'''a = 'y'
lst = []
for i in a.split():
    lst.append(i + ' ' + str(len(i)))
print(lst)'''
