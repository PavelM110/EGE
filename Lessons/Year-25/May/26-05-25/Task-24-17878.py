from re import *

with open('24_17878.txt') as file:
    data = file.readline()

num = r'([6789]\d*|0)'
pat = rf'{num}([*-]{num})*'

matches = [i.group() for i in finditer(pat, data)]

print(len(max(matches, key=len)))