with open('17_13882.txt') as file:
    data = [int(i) for i in file if i]

max_401 = max(i for i in data if i % 401 == 0)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i + 3]
    sa = sum(map(int, str(a)))
    sb = sum(map(int, str(b)))
    sc = sum(map(int, str(c)))
    u1 = len({sa, sb, sc}) == 3
    summ = a + b + c
    u2 = summ > max_401
    if u1 and u2: ans.append(summ)

print(len(ans), min(ans))