def f(n):
    d = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: d |= {i, n // i}
    return max(d) + min(d) if d else 0

cnt = 5

for i in range(800_001, 10**10):
    m = f(i)
    if m % 10 == 4:
        print(i, m)
        cnt -= 1
        if not cnt: break