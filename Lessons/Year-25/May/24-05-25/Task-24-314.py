from re import *

with open('24-314.txt') as file:
    data = file.readline()

num = r'([1-5][0-5]*|0)'
pat = fr'{num}([+*]{num})*'

matches = [i.group() for i in finditer(pat, data)]
maxx = len(max(matches, key=len))

ans = []
pat1 = r'\d+'
for match in matches:
    if len(match) == maxx:
        for i in finditer(pat1, match):
            i = i.group()
            match = match.replace(i, str(int(i, 6)), 1)
        ans.append(eval(match))

print(max(ans) % 1_000_000)
