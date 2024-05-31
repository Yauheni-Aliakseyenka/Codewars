'''
Your classmates asked you to copy some paperwork for them.
You know that there are 'n' classmates and the paperwork has 'm' pages.
Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
'''

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

def paperwork1(n, m):
    return max(n, 0)*max(m, 0)

n = int(input())
m = int(input())

print(paperwork(n, m))