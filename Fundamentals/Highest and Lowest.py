'''
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.
'''


def high_and_low(numbers):
    new_row = ''
    lst = numbers.split(' ')
    new_row = str(max(map(int, lst))) + ' ' + str(min(map(int, lst)))
    return new_row


def high_and_low1(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))


def high_and_low2(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])


numbers = '1 2 3 4 54 6'

print(high_and_low(numbers))
