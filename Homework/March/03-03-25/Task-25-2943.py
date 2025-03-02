def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs)
    if divs:
        return divs[0] + divs[-1]
    return 0

cnt = 5

for n in range(220_001, 10**20):
    m = f(n)
    if m % 10 == 4:
        print(n, m)
        cnt -= 1
        if not cnt:
            break