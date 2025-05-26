from re import *

with open('24_20813 (1).txt') as file:
    data = file.readline()

num = r'([789]\d*|0)'
pat = rf'{num}([*-]{num})*'

matches = [i.group() for i in finditer(pat, data)]

print(len(max(matches, key=len)))