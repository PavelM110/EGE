with open('24_17535.txt') as file:
    data = file.readline()

data = data.split('CD')

ans = 0

for i in range(len(data) - 160):
    st = 'CD'.join(data[i:i+161])
    if i != 0 and i != len(data) - 159:
        ans = max(ans, len(st) + 2)
    else:
        ans = max(ans, len(st) + 1)

print(ans)