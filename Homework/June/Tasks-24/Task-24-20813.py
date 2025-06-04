from re import *

with open('24_20813.txt') as file:
    data = file.readline()

num = r'([789][0789]*|0)'
pat = rf'{num}([*-]{num})*'

print(len(max([i.group() for i in finditer(pat, data)], key=len)))