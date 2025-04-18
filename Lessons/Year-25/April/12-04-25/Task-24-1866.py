from re import *

with open('24_1866.txt') as file:
    data = file.readline()

pat = r'(((?<=a)d)|((?<=d)a)).+?((d(?=a))|(a(?=d)))'

ans = match('1', '1')

for i in finditer(pat, data):
    l = len(i.group())
    if l > len(ans.group()):
        ans = i

print(len(ans.group()))
print(ans.group())
print('ad' in ans.group())