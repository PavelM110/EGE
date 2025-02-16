def f(n):
    res = ''
    while n:
        res += str(n % 4)
        n //= 4
    return res[::-1]

for n in range(1, 1000)[::-1]:
    r = f(n)
    if len(r) % 2 == 0: r = r[:len(r)//2] + '0' + r[len(r)//2:]
    r = int(r)
    if r <= 180:
        print(n)
        break