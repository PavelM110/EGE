def m(m, n): return m % n

def f(a):
    for x in range(1, 1000):
        u = (a+x > 700-a) and (m(a, 100) + m(100, x) > 50)
        if not u: return False
    return True

for a in range(1, 500):
    if f(a):
        print(a)
        break