def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

ans = []

for n in range(1, 1000):
    r = f(n)
    if not n % 3: r += r[-2:]
    else: r += f(sum(map(int, r)))
    r = int(r, 3)
    if not r % 2 and r > 220:
        ans.append(r)

print(min(ans))