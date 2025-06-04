def d(n, m):
    return n % m == 0

def f(a):
    for x in range(1, 1_000_000):
        b = 70 <= x <= 90
        u = d(x, a) or (b <= (not d(x, 22)) )
        if not u: return False
    return True

for a in range(1000, -1, -1):
    if f(a):
        print(a)
        break