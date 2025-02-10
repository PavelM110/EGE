from string import ascii_uppercase

with open('24_14510.txt') as file:
    data = file.readline()

for i in 'EIYOU':
    data = data.replace(i, 'A')

for i in ascii_uppercase:
    if i not in 'AEIUOY':
        data = data.replace(i, 'B')

data = data.replace('BBA', '*')

data = data.split('*')

print(len(data))

ans = 10**18

for i in range(len(data) - 498):
    ans = min(ans, len('BBA'.join(data[i:i+499])))

print(ans + 6)