def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

ans = []

for n in range(1, 10_000):
    r = f(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += f((n % 3) * 4)
    r = int(r, 3)
    if r < 199:
        ans.append(n)

print(max(ans))