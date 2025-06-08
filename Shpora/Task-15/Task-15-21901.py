def f(a):
    for x in range(0, 1_000_000):
        u = ((x & 52 != 0) and (x & 48 == 0)) <= (not(x & a == 0))
        if not u: return False
    return True

for a in range(0, 1_000_000):
    if f(a):
        print(a)
        break