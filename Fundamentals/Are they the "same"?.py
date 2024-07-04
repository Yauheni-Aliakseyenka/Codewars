'''
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether
the two arrays have the "same" elements, with the same multiplicities (the multiplicity
of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
'''


def comp(array1, array2):
    if array1 == array2 == []:
        return True
    elif array1 == [] or array2 == []:
        return False
    else:
        return sorted(list(map((lambda x: x ** 2), array1))) == sorted(array2)


def comp1(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


def comp2(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)] == sorted(a2)


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

#print(list(map((lambda x: x ** 2), sorted(a))))

'''count = 0
for i in set(b):
    for j in set(a):
        if i // j == j:
            count += 1
if count == len(set(b)):
    print(True)
else:
    print(False)'''

if list(map((lambda x: x ** 2), sorted(a))) == sorted(b):
    print(True)
else:
    print(False)