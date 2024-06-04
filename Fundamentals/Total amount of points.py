'''
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings.
Each match is represented by a string in the format "x:y",
where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns
the number of points our team (x) got in the championship by the rules given above.

Notes:
our team always plays 10 matches in the championship

0 <= x <= 4
0 <= y <= 4
'''

games = ['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']

score = 0
for i in games:
    a = i.split(':')
    if a[0] > a[1]:
        score += 3
    elif a[0] == a[1]:
        score += 1
print(score)

for i in games:
    if int(i[0]) > int(i[2]):
        score += 3
    elif int(i[0]) == int(i[2]):
        score += 1
print(score)

def points(games):
    score = 0
    for i in games:
        if i[0] > i[2]:
            score += 3
        elif i[0] == i[2]:
            score += 1
    return score

def points1(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))