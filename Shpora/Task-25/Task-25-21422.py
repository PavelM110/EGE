def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs)
    divs = [i for i in divs if i > 7 and i % 10 == 7]
    return min(divs) if len(divs) else 0

cnt = 5

for i in range(1_125_001, 10**10):
    d = f(i)
    if d:
        print(i, d)
        cnt -= 1
        if not cnt: break