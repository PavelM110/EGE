with open('24_15339.txt') as file:
    data = file.readline()

for i in 'BC':
    data = data.replace(i, 'A')

for i in '789':
    data = data.replace(i, '6')

data = data.replace('AA', 'A A')
data = data.replace('66', '6 6')

data = data.split()

print(len(max(data, key=len)))