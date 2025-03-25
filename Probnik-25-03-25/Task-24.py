with open('2418.txt') as file:
    data = file.readline()

for i in '3579':
    data = data.replace(i, '1')

for i in '468':
    data = data.replace(i, '2')

data = data.replace('-', '*')

data = data.replace('**', ' ').replace(' *', ' ').replace('* ', ' ')

while ' 00' in data:
    data = data.replace(' 00', ' 0 0')

data = data.replace(' 01', ' 0 1').replace(' 02', ' 0 2')

while '1*' in data or '1 ' in data:
    data = data.replace('1*', ' ').replace('1 ', ' ')

data = data.split()

print(len(max(data, key=len)))