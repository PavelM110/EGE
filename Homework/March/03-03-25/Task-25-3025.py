def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if i % 2:
                divs.add(i)
            if (n // i) % 2:
                divs.add(n // i)
    if len(divs) >= 6:
        divs = sorted(divs, reverse=True)
        return divs[5]
    return 0

cnt = 5

for n in range(200_000_001, 10**20):
    d = f(n)
    if d:
        print(n, d)
        cnt -= 1
        if not cnt: break