from re import *

with open('24_17563.txt') as file:
    data = file.readline()

num = r'([789]\d*)'

pat = rf'{num}([*-]{num})*'

matches = [i.group() for i in finditer(pat, data)]

print(len(max(matches, key=len)))

data = data.replace('-', '*')
data = data.replace('8', '7').replace('9', '7')

data = data.replace('**', ' ') # Два занка рядом

while ' 0' in data or ' 07' in data: data = data.replace(' 0', ' ').replace(' 07', ' 7') # Ведущие нули без знакка
while '*0' in data or '*07' in data: data = data.replace('*0', ' ').replace('*07', '*7') # Ведущие нули со знаком

data = data.split()

print(len(max(data, key=len)))