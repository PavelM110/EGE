def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    if len(divs):
        return max(divs) - min(divs)
    return 0

cnt = 5

for i in range(300_001, 10**20):
    m = f(i)
    if m % 10 == 6:
        print(i, m)
        cnt -= 1
        if cnt == 0:
            break