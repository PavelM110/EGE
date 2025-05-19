from re import *

with open('24_4643.txt') as file:
    data = file.readline()

pat = r'(\d\d[AB])*'

matches = finditer(pat, data)

print(max([len(i.group()) for i in matches]) // 3)