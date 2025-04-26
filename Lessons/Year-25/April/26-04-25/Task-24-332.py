from re import *

with open('24-332.txt') as file:
    data = file.readline()

pat = r'[ABC][abc]*( [ABC]?[abc]+)*\.'

matches = finditer(pat, data)

ans = [0]

for i in matches:
    i = i.group()
    if len(i) > ans[0]:
        ans = [len(i), i]

print(ans)