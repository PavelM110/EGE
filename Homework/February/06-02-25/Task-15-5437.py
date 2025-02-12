def d(n, m): return n % m == 0

def f(a):
    for x in range(1, 500):
        for y in range(1, 500):
            for z in range(1, 500):
                u = (d(z, 115) or d(y, 78) or d(x, 51)) <= d(x, a)
                if not u: return False
    return True

for a in range(1, 100)[::-1]:
    if f(a):
        print(a)
        break