from re import *

with open('24.5_19717.txt') as file:
    data = file.readline()

not_M = r'([^M]*)'
M_278 = r'(?:M[^M]*){278}'
la_278_M = rf'(?=({M_278}))'
pat = rf'{not_M}{la_278_M}'

matches = findall(pat, data)

# ans = 0
#
# for match in matches:
#     ans = max(ans, len(match.group()))
#
# print(ans)

res = max([len(match[0] + match[1])
           for match in matches])
print(res)

ans = 0

data = data.split('M')

for i in range(len(data) - 278):
    st = 'M'.join(data[i:i+279])
    ans = max(ans, len(st))

print(ans)