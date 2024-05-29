'''Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).'''

sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(sheeps):
    count = 0
    for i in sheeps:
        if i:
            count += 1
    return count

def count_new(sheeps):
    return sheeps.count(True)

print(count_new(sheeps))