def f(n):
    res = ''
    while n:
        res += str(n % 4)
        n //= 4
    return res[::-1]

ans = []

for n in range(1, 1000):
    r = f(n)
    if sum(map(int, r)) % 2 == 0:
        r += r[-2:]
    else:
        r = '2' + r + '0'
    r = int(r, 4)
    if r > 120 and r % 2 == 0:
        ans.append(r)

print(min(ans))