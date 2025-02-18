with open('24.txt') as file:
    data = file.readline()

data = data.replace('RSQ', '@@@')
data = data.replace('Q@', '@@').replace('S@', '@@')
data = data.replace('@R', '@@').replace('@S', '@@')

data = data.replace('R', ' ').replace('S', ' ').replace('Q', ' ')

data = data.split()

print(len(max(data, key=len)))