'''
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
'''
def digitize(n):
    a = []
    for i in str(n):
        a.append(int(i))
    return a[::-1]

def digitize_new(n):
    return map(int, str(n)[::-1])

n = input()
print(list(digitize_new(n)))