with open('24_20909.txt') as file:
    data = file.readline()

data = data.split('AB')

ans = 0

for i in range(len(data) - 100):
    st = 'AB'.join(data[i:i+101])
    if i != 0 and i != len(data) - 100 - 1:
        ans = max(ans, len(st) + 2)
    else: ans = max(ans, len(st) + 1)

print(ans)