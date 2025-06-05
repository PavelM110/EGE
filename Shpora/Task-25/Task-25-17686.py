def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if i % 10 == 7 and i != 7: divs |= {i}
            if (n // i) % 10 == 7 and n // i != 7: divs |= {n // i}
    if len(divs) != 0: return min(divs)
    return 0

cnt = 5

for i in range(700_001, 10**10):
    d = f(i)
    if d:
        print(i, d)
        cnt -= 1
        if not cnt: break