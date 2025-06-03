from re import *

with open('24_15339.txt') as file:
    data = file.readline()

pat = r'[ABC]?([6789][ABC])+[6789]?'

matches = [i.group() for i in finditer(pat, data)]

print(len(max(matches, key=len)))