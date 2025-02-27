def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs)
    if len(divs) >= 7:
        return divs[-7], len(divs)
    return 0, 0

cnt = 5

for i in range(400_000_001, 10**20):
    d, l = f(i)
    if d:
        print(d, l)
        cnt -= 1
        if cnt == 0: break