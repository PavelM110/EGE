def d(n, m):
    return n % m == 0

def f(a):
    for x in range(1, 1000):
        f = (d(a, x) <= ((x == a) or (x == 1)))
        if not f:
            return False
    return True

cnt = 0

for a in range(1, 11112):
    if f(a): cnt += 1

print(cnt)