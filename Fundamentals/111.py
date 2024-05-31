a = ['hgjg', 22, 929]

b = ';'.join(map(lambda i: str(i), a))

c = ';'.join(map(str, a))

print(b)
print(c)