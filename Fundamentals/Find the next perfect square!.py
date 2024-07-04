'''
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1
or an empty value like None or null, depending on your language. You may assume the argument is non-negative.
'''


def find_next_square(sq):
    return (sq ** 0.5 + 1) ** 2 if (sq ** 0.5).is_integer() else -1

    if sq ** 0.5 == int:
        return (sq ** 0.5 + 1) ** 2
    else:
        return -1


def find_next_square1(sq):
    x = sq**0.5
    return -1 if x % 1 else (x+1)**2


a = 120

print(a ** 0.5 % 1)