def d(n, m):
    return n % m == 0

def f(a):
    for x in range(1, 1_000_000):
        u = (not d(x, a)) <= (d(x, 28) <= (not d(x, 49)))
        if not u: return False
    return True

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break