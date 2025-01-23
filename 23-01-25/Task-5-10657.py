def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

for n in range(1, 1000)[::-1]:
    r = f(n)
    if sum(map(int, r)) % 3 == 0:
        r = '20' + r
    else:
        r = '10' + r
    r = int(r, 3)
    if r < 100:
        print(n)
        break