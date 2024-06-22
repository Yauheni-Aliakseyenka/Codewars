'''
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with "*" character.
For example, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ",
  "*****"
]
'''


def tower_builder(n_floors):
    i = 1
    tower = []
    while n_floors:
        tower.append(str(' ' * (n_floors - 1) + '*' * i + ' ' * (n_floors - 1)))
        i += 2
        n_floors -= 1
    return tower


def tower_builder2(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


n = int(input())
print(tower_builder(n))