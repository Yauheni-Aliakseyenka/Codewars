'''

'''


'''n = int(input())
x1 = 0
x2 = 1
x = x1 * x2
while n > x:
    x1, x2 = x2, x1 + x2
    if n == x1 * x2:
        flag = True
    else:
        flag = False
    x = x1 * x2


print(x1, x2, flag)'''


def product_fib(_prod):
    x1 = 0
    x2 = 1
    while _prod > x1 * x2:
        x1, x2 = x2, x1 + x2
    return [x1, x2, _prod == x1 * x2]

