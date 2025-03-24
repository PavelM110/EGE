with open('24_4682.txt') as file:
    data = file.readline()

data = data.replace('E', 'A').replace('C', 'B').replace('D', 'B')

data = data.replace('AB', '@').replace('B', ' ').replace('A', ' ')

data = data.split()

print(len(max(data, key=len)))