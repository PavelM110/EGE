from re import *

with open('24_2942.txt') as file:
    data = file.readline()

pat = r'((AB)|(AC))+'

matches = finditer(pat, data)

print(len(max([i.group() for i in matches], key=len)) // 2)

data = data.replace('AB', '@').replace('AC', '@')
for i in 'ABC': data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))