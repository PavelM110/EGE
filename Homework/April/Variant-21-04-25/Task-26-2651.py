from itertools import groupby

with open('26_2651.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

data1 = groupby(data, key=lambda x: x[0])

marks = [[] for i in range(1992)]

for k, g in data1:
    for i in g:
        marks[k].append(i[1])

for i in range(len(marks)):
    marks[i] = 8 - len(set(marks[i]))

ans_marks = []

ans1 = 0

for i in range(1961, 1992):
    ans1 += marks[i]

for i in range(1961, 1992):
    ans_marks.append((marks[i], i))

print(ans1)
print(max(ans_marks))