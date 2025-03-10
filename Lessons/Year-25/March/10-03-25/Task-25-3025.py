def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if i % 2: divs.add(i)
            if (n // i) % 2: divs.add(n // i)
    divs = sorted(divs)
    if len(divs) < 6: return 0
    return divs[-6]

cnt = 5

for i in range(200_000_001, 10**20):
    d = f(i)
    if d:
        print(i, d)
        cnt -= 1
        if not cnt: break