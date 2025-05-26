from re import *

with open('24_21908.txt') as file:
    data = file.readline()

pat = r'[1-9ABCD][0-9ABCD]*[02468AC]'

matches = [i.group() for i in finditer(pat, data)]

ans = 0

for match in matches:
    for l in range(len(match)):
        for r in range(len(match) + 1, l, -1):
            st = match[l:r]
            if int(st, 14) % 2 == 0:
                ans = max(ans, len(st))
                break

print(ans)