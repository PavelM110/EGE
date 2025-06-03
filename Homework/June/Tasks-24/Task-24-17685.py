from re import *

with open('24_17685.txt') as file:
    data = file.readline()

num = r'([1-9]\d*|0)'

pat = rf'{num}([+*]{num})*'

matches = [i.group() for i in finditer(pat, data)]

ans = 0

for match in matches:
    if eval(match) == 0: ans = max(ans, len(match))
    else:
        flag = False
        for l in range(len(match)):
            if flag: break
            for r in range(len(match), l, -1):
                st = match[l:r]
                st = st.strip('+*').lstrip('0')
                if st and st[0] in '+*': st = '0' + st
                if st and eval(st) == 0:
                    ans = max(ans, len(st))
                    flag = True
                    break

print(ans)