from re import *

with open('24_9845 (1).txt') as file:
    data = file.readline()

pat = r'[89]?([ABC][89])+[ABC]?'

matches = finditer(pat, data)

print(len(max([i.group() for i in matches], key=len)))

data = data.replace('8', '9')
data = data.replace('99', '9 9').replace('99', '9 9')
for i in 'BC':data =  data.replace(i, 'A')
data = data.replace('AA', 'A A').replace('AA', 'A A')
data = data.split()

print(len(max(data, key=len)))