def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs, reverse=True)
    return divs if len(divs) >= 7 else 0

cnt = 5

for i in range(400_000_001, 10**20):
    d = f(i)
    if d:
        print(d[6], len(d))
        cnt -= 1
        if not cnt: break