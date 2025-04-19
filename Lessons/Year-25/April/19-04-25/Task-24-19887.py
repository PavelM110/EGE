from re import *

with open('24.23_19887.txt') as file:
    data = file.readline()

pat = r'[13579]?([02468][13579])*[02468]?'

matches = finditer(pat, data)

print(max(len(i.group()) for i in matches))