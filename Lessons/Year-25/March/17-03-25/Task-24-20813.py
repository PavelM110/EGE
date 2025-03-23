with open('24_20813.txt') as file:
    data = file.readline()

data = data.replace('-', '*')
data = data.replace('7', '8').replace('9', '8')

data = data.replace('**', ' ').replace('**', ' ')
data = data.replace('*08', '*0 8').replace(' 08', ' 0 8')
data = data.replace('*00', '*0 0')
while ' 00' in data: data = data.replace(' 00', ' 0 0')
data = data.split()

ans = 0

for i in data:
    ans = max(ans, len(i))

print(ans)