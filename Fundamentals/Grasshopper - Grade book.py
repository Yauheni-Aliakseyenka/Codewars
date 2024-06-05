'''
Complete the function so that it finds the average of the three scores passed to it
and returns the letter value associated with that grade.
'''

def get_grade(s1, s2, s3):
    s = (s1 + s2 + s3) / 3
    if 90 <= s <= 100:
        return 'A'
    elif 80 <= s < 90:
        return 'B'
    elif 70 <= s < 80:
        return 'C'
    elif 60 <= s < 70:
        return 'D'
    elif 0 <= s < 60:
        return 'F'

def get_grade1(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')

a = int(input())
b = int(input())
c = int(input())

print(get_grade(a, b, c))

