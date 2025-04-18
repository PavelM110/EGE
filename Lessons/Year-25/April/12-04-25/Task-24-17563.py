from re import *

with open('24_17563.txt') as file:
    data = file.readline()

pat = r'[1-9]\d*([\-\*]([1-9]\d*))*'

matches = finditer(pat, data)

matches = [i.group() for i in matches]

print(len(max(matches, key=len)))