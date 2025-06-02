def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

ans = []

for n in range(3, 10_000):
    r = f(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += f((n % 3) * 3)
    r = int(r, 3)
    if r <= 150: ans.append(n)

print(max(ans))