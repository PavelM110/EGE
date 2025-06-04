from re import *

with open('24_21421.txt') as file:
    data = file.readline()

pat = r'[1-9AB][0-9AB]*[02468A]'

print(len(max([i.group() for i in finditer(pat, data)], key=len)))