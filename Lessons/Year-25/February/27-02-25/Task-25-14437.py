def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    if divs:
        return sum(divs) // len(divs)
    return 0

cnt = 0

for i in range(700_001)[::-1]:
    m = f(i)
    if m % 1000 == 313:
        print(i, m)
        cnt += 1
        if cnt == 7: break