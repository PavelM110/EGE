def d(n, m): return n % m == 0

def f(a):
    for x in range(1, 1000):
        u = d(x, 17) <= (not(x in range(80, 101)) or (a < x+30))
        if not u: return False
    return True

for a in range(1, 200)[::-1]:
    if f(a):
        print(a)
        break