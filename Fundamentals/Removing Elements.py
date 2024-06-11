'''
Take an array and remove every second element from the array.
Always keep the first element and start removing with the next element.

None of the arrays will be empty, so you don't have to worry about that!
'''


def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if not i % 2]


def remove_every_other1(my_list):
    return my_list[::2]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_every_other(a))