from re import *

with open('24_4643.txt') as file:
    data = file.readline()

pat = r'(\d\d[AB])*'

matches = finditer(pat, data)

print(max([len(i.group()) for i in matches]) // 3)

data = data.replace('2', '1').replace('B', 'A')
data = data.replace('11A', '@').replace('A', ' ').replace('1', ' ')
data = data.split()

print(len(max(data, key=len)))