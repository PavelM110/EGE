from re import *

with open('24.5_19717.txt') as file:
    data = file.readline()

pat = r'(?<=[M/A])([AEGILR]*+M){278}[AEGILR]*+(?=[M/Z])'

matches = finditer(pat, data)

ans = 0

for match in matches:
    ans = max(ans, len(match.group()))

print(ans)

ans = 0

data = data.split('M')

for i in range(len(data) - 278):
    st = 'M'.join(data[i:i+279])
    ans = max(ans, len(st))

print(ans)