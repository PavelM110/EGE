with open('24_7662.txt') as file:
    data = file.readline()

data1 = data
data = data.split('SOLO')


ans = ''

for i in range(len(data) - 4):
    st = 'SOLO'.join(data[i:i+5])
    cnt = 0
    for i in '0123456789':
        if i in st: cnt += 1
    if cnt >= 5:
        if len(ans) < len(st):
            ans = st

print(len(ans), data1.find(ans))