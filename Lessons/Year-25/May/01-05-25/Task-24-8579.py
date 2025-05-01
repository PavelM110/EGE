from re import *

with open('24_8579.txt') as file:
    data = file.readline()

pat = (r'([13579]\D+[02468])|([02468]\D+[13579])')

matches = finditer(pat, data)

ans = 0

for i in matches:
    ans = max(ans, len(i.group()))

print(ans)


for i in '3579': data = data.replace(i, '1')
data = data.replace('1', '1 1')
for i in '2468': data = data.replace(i, '0')
data = data.replace('0', '0 0')

data = data.split()

ans1 = 0

for i in data:
    if i[0] in '0123456789' and i[-1] in '0123456789':
        if int(i[0]) % 2 != int(i[-1]) % 2:
            ans1 = max(ans1, len(i))

print(ans1)















