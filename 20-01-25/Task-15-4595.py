def d(m, n):
    return m % n == 0

def f(a):
    for x in range(1, 10_000):
        u = (d(x, 2) <= (not(d(x, 3)))) or (x + a >= 80)
        if not u:
            return False
    return True

for a in range(1, 100_000):
    if f(a):
        print(a)
        break