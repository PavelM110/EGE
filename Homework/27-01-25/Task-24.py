with open('24_8510.txt') as file:
    data = file.readline()

for i in 'NOP':
    for j in 'NOP':
        data = data.replace(i+j, i+' '+j)

data = data.split()

print(len(max(data, key=len)))