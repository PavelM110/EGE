from string import ascii_uppercase
from re import *

with open('24_9791 (1).txt') as file:
    data = file.readline()

pat = r'[1-9A-F][\dA-F]*'

matches = finditer(pat, data)

print(max([len(i.group()) for i in matches]))


for i in ascii_uppercase[6:]:
    data = data.replace(i, ' ')

while ' 0' in data:
    data = data.replace(' 0', ' ')
data = data.split()

print(len(max(data, key=len)))



