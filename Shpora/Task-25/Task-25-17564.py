def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: divs |= {i, n // i}
    divs = sorted(divs)
    if len(divs) > 1:
        return max(divs) + min(divs)
    return 0

cnt = 5

for i in range(700_001, 10**10):
    m = f(i)
    if m % 10 == 4:
        cnt -= 1
        print(i, m)
        if not cnt: break