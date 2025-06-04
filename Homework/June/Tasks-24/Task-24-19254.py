with open('24_19254 (1).txt') as file:
    data = file.readline()

data = data.split('FSRQ')

ans = 0

for i in range(len(data) - 80):
    st = 'FSRQ'.join(data[i:i+81])
    if i != 0 and i != len(data) - 80 - 1:
        ans = max(ans, len(st) + 6)
    else:
        ans = max(ans, len(st) + 3)

print(ans)