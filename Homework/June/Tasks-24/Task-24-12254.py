from re import *

with open('24_12254.txt') as file:
    data = file.readline()

pat = r'(SQ|Q)?(RSQ)+(RS|R)?'

matches = [i.group() for i in finditer(pat, data)]

print(len(max(matches, key=len)))

data = data.replace('RSQ', '@@@')
data = data.replace('SQ@', ' @@@')
data = data.replace('@RS', '@@@ ')
data = data.replace('Q@', ' @@')
data = data.replace('@R', '@@ ')

for i in 'RSQ':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))