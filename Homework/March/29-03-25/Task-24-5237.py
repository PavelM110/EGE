with open('24_5237.txt') as file:
    data = file.readline()

data = data.replace('Z',  ' ').replace('XX', 'X X').replace('YY', 'Y Y')

data = data.split()

print(len(max(data, key=len)))