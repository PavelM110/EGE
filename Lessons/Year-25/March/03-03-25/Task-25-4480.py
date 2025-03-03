def f(n):
    divs = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs)
    return divs

cnt = 6

for n in range(800_001, 10**20):
    divs = f(n)
    summ = sum(divs)
    prod = 1
    for i in divs: prod *= i
    if summ % 2 == 1 and prod % 2 == 1 and len(divs) > 10:
        print(n, len(divs))
        cnt -= 1
        if not cnt: break