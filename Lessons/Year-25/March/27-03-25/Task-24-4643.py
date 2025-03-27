from itertools import groupby

with open('24_4643.txt') as file:
    data = file.readline()

data = data.replace('2', '1').replace('B', 'A')

data = data.replace('11A', '*')

print(len(max([list(g) for k, g in groupby(data) if k == '*'], key=len)))

data = data.replace('1', ' ').replace('A', ' ')

data = data.split()

print(len(max(data, key=len)))