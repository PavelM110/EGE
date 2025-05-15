from re import *

with open('24_4627.txt') as file:
    data = file.readline()

pat = r'((NPO)|(PNO))+'

matches = finditer(pat, data)

print(len(max([i.group() for i in matches], key=len)) // 3)

data = data.replace('NPO', '@').replace('PNO', '@')
for i in 'NPO': data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))