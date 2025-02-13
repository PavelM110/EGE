def d(n, m): return n % m == 0

def f(a):
    for x in range(1, 1000):
        u = (not d(x, a)) <= (d(x, 14) <= (not d(x, 4)))
        if not u: return False
    return True

for a in range(1, 100)[::-1]:
    if f(a):
        print(a)
        break