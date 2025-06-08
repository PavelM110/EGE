def f(n):
    divs = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    return sum(divs) if len(divs) else 0

cnt = 5

for i in range(500_001, 10**10):
    r = f(i)
    if r % 10 == 6:
        print(i, r)
        cnt -= 1
        if not cnt: break