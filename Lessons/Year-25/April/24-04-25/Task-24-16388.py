from re import *

with open('24_16388.txt') as file:
    data = file.readline()

pat = r'(KLMN|LMN|MN|N)(KLMN)+(KLMN|KLM|KL|K)'

matches = finditer(pat, data)

ans = 0

for i in matches:
    ans = max(ans, len(i.group()))

print(ans)