def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

res = []

for n in range(11, 10_000):
    r = f(n)
    if (r.count('2') + r.count('0')) > r.count('1'):
        r = '22' + r
    else: r = '11' + r
    r = int(r, 3)
    if r > 100:
        res.append(r)

print(min(res))