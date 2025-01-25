with open('17_8562.txt') as file:
    data = [int(i) for i in file if i]

min_2 = 10000

def f1(n):
    return n**2 < min_2**2

for i in data:
    if len(str(i).strip('-')) == 2:
        min_2 = min(min_2, i)

print(min_2)

cnt = 0
ans = 10**18

for i in range(len(data) - 1):
    if f1(data[i]) ^ f1(data[i+1]):
        if data[i] + data[i + 1] >= 0:
            cnt += 1
            ans = min(ans, data[i] + data[i + 1])

print(cnt, ans)