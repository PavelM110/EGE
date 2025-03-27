def d(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    if len(divs):
        return sum(divs)
    return 0

cnt = 5

for i in range(1_273_548, 10**20):
    m = f(i)
    if m and d(m % 100_000):
        print(i, m)
        cnt -= 1
        if not cnt:
            break