def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            u = (x*y < a) or (x < y) or (9 < x)
            if not u: return False
    return True

for a in range(0, 1000):
    if f(a):
        print(a)
        break