'''
Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.

'''

def flick_switch(lst):
    t = True
    f = False
    for i in range(len(lst)):
        if lst[i] == 'flick':
            t, f = f, t
        lst[i] = t
    return lst

def flick_switch1(lst):
    res, state = [], True
    for i in lst:
        if i == 'flick':
            state = not state
        res.append(state)
    return res


a = ['bicycle', 'jarmony', 'flick', 'sheep', 'flick']
print(flick_switch(a))
