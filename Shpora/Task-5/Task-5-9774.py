def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

ans = []

for n in range(1, 10_000):
    r = f(n)
    o = n % 3
    if o == 0:
        r += r[-2:]
    else: r += f(o * 5)
    r = int(r, 3)
    if r > 133: ans.append(r)

print(min(ans))