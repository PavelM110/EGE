def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

res = []

for n in range(1, 10_000):
    r = f(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += f(sum(int(i) for i in r), 3)
    r = int(r, 3)
    if r % 2 == 0 and r > 220:
        res.append(r)

print(min(res))