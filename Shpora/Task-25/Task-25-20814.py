def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: divs |= {i, n // i}
    if len(divs): return sum(divs)
    return 0

cnt = 5

for i in range(500_001, 10**10):
    r = f(i)
    if r % 10 == 9:
        print(i, r)
        cnt -= 1
        if not cnt: break