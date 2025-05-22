from re import *

with open('24_17641.txt') as file:
    data = file.readline()

num = r'([1-9]\d*|0)'

pat = rf'{num}([\+\*]{num})*'

matches = finditer(pat, data)

ans = 0

for i in matches:
    i = i.group()
    if eval(i) == 0:
        ans = max(ans, len(i))
        continue
    for j in range(len(i)):
        for k in range(j+1, len(i))[::-1]:
            st = i[j:k+1]
            st = st.rstrip('+').rstrip('*')
            if st[:2] != '0+' and st[:2] != '0*' and st[0] not in '789': continue
            if eval(st) == 0:
                ans = max(ans, len(st))
                break

print(ans)