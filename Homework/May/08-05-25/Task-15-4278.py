def d(n, m):
    return n % m == 0

def f(a):
    for x in range(1, 1_000_000):
        u = d(a, 12) and (d(530, x) <= ((not d(a, x)) <= (not d(170, x))))
        if not u: return False
    return True

cnt = 0

for a in range(1, 1001):
    if f(a): cnt += 1

print(cnt)