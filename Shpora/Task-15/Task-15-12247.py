def f(a):
    for x in range(1, 1_000_000):
        u = (x & a == 0) or (not(x&37 == 0)) or (not(x&12 == 0))
        if not u: return False
    return True

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break