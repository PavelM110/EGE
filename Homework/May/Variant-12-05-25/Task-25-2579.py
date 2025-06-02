def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs)
    if len(divs) >= 3:
        return divs[-1] + divs[-2] + divs[-3]
    return 0

cnt = 5

for i in range(10_000_001, 10**18):
    s = f(i)
    if s and int(s ** .5) == s ** .5:
        print(s)
        cnt -= 1
        if not cnt:
            break