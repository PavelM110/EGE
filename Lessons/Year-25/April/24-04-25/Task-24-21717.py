with open('24_21717.txt') as file:
    data = file.readline()

# data = '@WWWWWWWW@W@W@WWWWWWWWWWWWW'

data = data.split('RSQ')

ans = [10**20]

for i in range(len(data) - 128):
    st = 'RSQ'.join(data[i:i+129])

    if len(st) < ans[0]:
        ans = [len(st), i, i + 128]

print(ans)
print(len(data))