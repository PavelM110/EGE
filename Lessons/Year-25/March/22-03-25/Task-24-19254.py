with open('24_19254.txt') as file:
    data = file.readline()

data = data.replace('FSRQ',  ' ')

data = data.split()

ans = [0, 0]

print(len(data))

for i in range(len(data) - 80):
    st = 'FSRQ'.join(data[i:i+81])
    if len(st) > ans[0]:
        ans = [len(st), i]

print(ans)