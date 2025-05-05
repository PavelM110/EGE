def f(n):
    res = ''
    while n:
        res += str(n % 5)
        n //= 5
    return res[::-1]

for n in range(1, 1000):
    r = f(n)
    l = len(r)
    if l % 2 == 1:
        r += str(n % 5)
    l = len(r)
    r = r[l//2:] + r[:l//2]
    r = int(r, 5)
    if r > 50:
        print(n)
        break