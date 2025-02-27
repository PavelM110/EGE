def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(i for i in divs if i % 2 == 1)
    if len(divs) == 3:
        return divs
    return 0, 0, 0

for i in range(18_782, 18_823):
    a, b, c = f(i)
    if a and b and c:
        print(a, b, c)