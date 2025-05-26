from re import *

with open('24_21421 (1).txt') as file:
    data = file.readline()

pat = r'[1-9AB][0-9AB]*[02468A]'

matches = [i.group() for i in finditer(pat, data)]

print(len(max(matches, key=len)))