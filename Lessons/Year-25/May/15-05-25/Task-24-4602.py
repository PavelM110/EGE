from re import *

with open('24_4602.txt') as file:
    data = file.readline()

pat = r'([BCD][AO])+'

matches = finditer(pat, data)

print(len(max([i.group() for i in matches], key=len)) // 2)

for i in 'CD': data = data.replace(i, 'B')
data = data.replace('O', 'A')
data = data.replace('BA', '@')
for i in 'ABCDO': data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))