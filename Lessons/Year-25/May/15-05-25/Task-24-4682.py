from re import *

with open('24_4682.txt') as file:
    data = file.readline()

pat = r'([AE][BCD])+'

matches = finditer(pat, data)

print(len(max([i.group() for i in matches], key=len)) // 2)

for i in 'CD': data = data.replace(i, 'B')
data = data.replace('E', 'A')
data = data.replace('AB', '@')
for i in 'ABCDE': data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))