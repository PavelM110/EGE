def f(n):
    divs = set()
    for i in range(2, int(n **.5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs)
    if len(divs) >= 2: return divs[-1] + divs[-2]
    return 0

for i in range(112_500_000, 112_550_001):
    m = f(i)
    if m % 10_000 == 1214:
        print(i)