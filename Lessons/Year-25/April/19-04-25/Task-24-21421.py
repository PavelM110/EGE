from re import *

with open('24_21421.txt') as file:
    data = file.readline()

pat = r'[1-9][0-9AB]*[02468A]'

matches = finditer(pat, data)

ans = 0

for match in matches:
    ans = max(ans, len(match.group()))

print(ans)