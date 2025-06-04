from re import *

with open('24_21908.txt') as file:
    data =file.readline()

pat = r'[1-9ABCD][0-9ABCD]*[02468AC]'

print(len(max([i.group() for i in finditer(pat, data)], key=len)))