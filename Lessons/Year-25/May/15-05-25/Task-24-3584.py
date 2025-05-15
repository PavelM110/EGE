from re import *

with open('24_3584.txt') as file:
    data = file.readline()

pat = r'((BA)|(DA))+'

matches = finditer(pat, data)

print(len(max([i.group() for i in matches], key=len)) // 2)

data = data.replace('BA', '@').replace('DA', '@')
for i in 'ABD': data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))