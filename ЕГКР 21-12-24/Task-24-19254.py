with open('input.txt') as file:
    data = file.readline()

data1 = data.split('FSRQ')

ans = 0
ans_index = 0

for i in range(len(data1) - 80):
    st = 'FSRQ'.join(data1[i:i+81])
    if len(st) > ans:
        ans = max(len(st), ans)
        ans_index = data.find(st)

print(ans + 6, ans_index, len(data))