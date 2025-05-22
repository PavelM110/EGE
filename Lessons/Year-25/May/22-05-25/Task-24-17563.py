from re import *

with open('24_17563 (2).txt') as file:
    data = file.readline()

num = r'([789]\d*)'
pat = rf'{num}([\-\*]{num})*'

matches = finditer(pat, data)

print(len(max([i.group() for i in matches], key=len)))