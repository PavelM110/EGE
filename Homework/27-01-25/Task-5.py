def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

res = []

for n in range(1, 1000):
    r = f(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += f((n % 3) * 5)
    r = int(r, 3)
    if r > 133:
        res.append(r)

print(min(res))