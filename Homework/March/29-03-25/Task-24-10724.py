from string import ascii_uppercase

with open('24_10724.txt') as file:
    data = file.readline()

for i in ascii_uppercase[6:]:
    data = data.replace(i, ' ')

while ' 0' in data:
    data = data.replace(' 0', ' ')

data = data.split()

print(len(max(data, key=len)))