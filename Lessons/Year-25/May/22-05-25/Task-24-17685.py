from re import *

with open('24_17685.txt') as file:
    data = file.readline()

num = r'(0|[1-9]\d*)'
pat = fr'{num}([\+\*]{num})*'

matches = [i.group() for i in finditer(pat, data)]

ans = 0

for match in matches:
    if eval(match) == 0:
        ans = max(ans, len(match))
    else:
        for l in range(len(match)):
            for r in range(len(match), l, -1):
                st = match[l:r].rstrip('+*')
                if len(st) > 0 and (st[:2] == '0+' or st[:2] == '0*' or st[0] in '123456789'):
                    if eval(st) == 0:
                        ans = max(ans, len(st))
                        break

print(ans)