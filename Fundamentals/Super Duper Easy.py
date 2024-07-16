'''
Make a function that returns the value multiplied by 50 and increased by 6.
If the value entered is a string it should return "Error".
'''


def problem(a):
    return 'Error' if type(a) is str else a * 50 + 6


def problem1(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"


print(problem(1))
