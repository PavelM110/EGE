from re import *

with open('24_17563 (1).txt') as file:
    data = file.readline()

num = r'[\+|\*][789]\d*'

pat = rf'[789][0789]*([\+\*][789][0789]*)*'

matches = finditer(pat, data)

ans = 0

for i in matches:
    anas = max(ans, len(i.group()))

print(ans)