from re import *

with open('24_17878.txt') as file:
    data = file.readline()

num = r'([6-9]\d*|0)'
pat = rf'{num}([*-]{num})*'

print(len(max([i.group() for i in finditer(pat, data)], key=len)))