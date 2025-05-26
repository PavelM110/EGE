with open('24_6798.txt') as file:
    data =file.readline()

data = data.replace('A', 'O').replace('D', 'C').replace('F', 'C')
data = data.replace('COO', '@').replace('CCO', '@')
for i in 'AOCDF':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))