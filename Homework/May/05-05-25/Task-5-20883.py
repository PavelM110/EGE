def f(n):
    res = ''
    while n:
        res += str(n % 5)
        n //= 5
    return res[::-1]

ans = 1000

for n in range(1, 1000):
    r = f(n)
    if len(r) % 2: r += str(n % 5)
    r = r[len(r) // 2:] + r[:len(r) // 2]
    r = int(r, 5)
    if r > 50:
        ans = min(ans, n)

print(ans)