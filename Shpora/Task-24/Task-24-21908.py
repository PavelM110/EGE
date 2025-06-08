from re import *

with open('24_21908 (1).txt') as file:
    data = file.readline()

pat = r'[1-9ABCD][0-9ABCD]*[02468AC]'

matches = [i.group() for i in finditer(pat, data)]

print(len(max(matches, key=len)))

ans = 0

for match in matches:
    if int(match, 14) % 2 == 0:
        ans = max(ans, len(match))
    elif len(match) > ans:
        for l in range(len(match)):
            for r in range(len(match), l, -1):
                st = match[l:r].lstrip('0')
                if int(st, 14) % 2 == 0:
                    ans = max(ans, len(st))
                    break

print(ans)