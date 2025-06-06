def f(n):
    d = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: d |= {i, n // i}
    d = [i for i in d if i != 9 and i % 10 == 9]
    return min(d) if len(d) else 0

cnt = 5

for i in range(800_001, 10**10):
    d = f(i)
    if d:
        print(i, d)
        cnt -= 1
        if not cnt: break