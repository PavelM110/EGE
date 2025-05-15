from re import *

with open('24_1975.txt') as file:
    data = file.readline()

pat = r'[^R]*(R[^R]+)+R?'


matches = finditer(pat, data)

print(len(max([i.group() for i in matches], key=len)))

data = data.replace('RR', 'R R')
data = data.split()

print(len(max(data, key=len)))