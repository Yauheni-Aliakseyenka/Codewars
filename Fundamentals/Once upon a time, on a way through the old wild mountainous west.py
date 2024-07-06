'''
… a man was given directions to go from one point to another.
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort.
Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy,
otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place!
So the task is to give to the man a simplified version of the plan.

A better plan in this case is simply:
["WEST"]

Write a function dirReduc which will take an array of strings and returns an array of strings
with the needless directions removed (W<->E or S<->N side by side).
'''


def dir_reduc(arr):
    dct = {'EAST': 'WEST', 'NORTH': 'SOUTH', 'WEST': 'EAST', 'SOUTH': 'NORTH'}
    j = 0
    if not arr:
        return []
    while len(arr) != j + 1:
        if dct[arr[j]] == arr[j - len(arr) + 1]:
            del arr[j:j + 2]
            if j >= len(arr):
                break
            j = 0
        else:
            j += 1
    return arr


opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}


def dirReduc1(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


def dirReduc2(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

a = ['WEST', 'WEST', 'NORTH', 'WEST', 'NORTH', 'NORTH', 'WEST', 'WEST', 'WEST', 'WEST', 'SOUTH', 'EAST']






