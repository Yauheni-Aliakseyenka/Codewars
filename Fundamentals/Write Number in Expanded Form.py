'''
You will be given a number and you will need to return it as a string in Expanded Form.
NOTE: All numbers will be whole numbers greater than 0.
'''


a = int(input())
b = []

for i, n in enumerate(str(a)[::-1]):
    if int(n) != 0:
        b.append(n + ('0' * i))

print(' + '.join(b[::-1]))





