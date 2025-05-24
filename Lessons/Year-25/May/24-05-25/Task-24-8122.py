from re import *

with open('24-347.txt') as file:
    data = file.readline()

pat = r'[1-9AB][0-9AB]*'

matches = finditer(pat, data)

ans = []

for match in matches:
    if int(match.group(), 12) % 6 == 0:
        ans.append(match.group())
    else:
        for l in range(len(match.group())):
            for r in range(len(match.group()), l, -1):
                st =  match.group()[l:r]
                if st[0] != '0':
                    if int(st, 12) % 6 == 0:
                        ans.append(st)
                else:
                    break

max_str = max(ans, key=len)

print(data.find(max_str) + len(max_str) - 1)