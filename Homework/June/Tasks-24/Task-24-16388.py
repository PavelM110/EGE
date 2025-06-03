from re import *

with open('24_16388.txt') as file:
    data = file.readline()

pat = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'

matches = [i.group() for i in finditer(pat, data)]

print(len(max(matches, key=len)))

data = data.replace('KLMN', '@@@@')
data = data.replace('@KLM', '@@@@ ')
data = data.replace('@KL', '@@@ ')
data = data.replace('@K', '@@ ')
data = data.replace('LMN@', ' @@@@')
data = data.replace('MN@', ' @@@')
data = data.replace('N@', ' @@')

for i in 'KLMN': data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))