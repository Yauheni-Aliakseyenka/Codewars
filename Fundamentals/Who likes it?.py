'''
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
'''


def likes(a):
    str1 = ' likes this'
    str2 = ' like this'
    str3 = ' others like this'
    if len(a) == 0:
        return 'no one' + str1
    elif len(a) == 1:
        return f'{a[0]} ' + str1
    elif len(a) == 2:
        return a[0] + ' and ' + a[1] + str2
    elif len(a) == 3:
        return f'{a[0]}, {a[1]} and {a[2]}' + str2
    elif len(a) > 3:
        return f'{a[0]}, {a[1]} and {len(a[2::])}' + str3


a = ["Alex", "Jacob", "Mark", "Max"]

str1 = ' likes this'
str2 = ' like this'
str3 = ' others like this'

if len(a) == 0:
   print('no one' + str1)
elif len(a) == 1:
    print(f'{a[0]} ' + str1)
elif len(a) == 2:
    print(a[0] + ' and ' + a[1] + str2)
elif len(a) == 3:
    print(f'{a[0]}, {a[1]} and {a[2]}' + str2)
elif len(a) > 3:
    print(f'{a[0]}, {a[1]} and {len(a[2::])}' + str3)


def likes1(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.

    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4

    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others=length - 2)