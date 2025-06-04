def f(a):
    for x in range(0, 1_000):
        for y in range(1, 1_000):
            u = (5 < y) or (x > 32) or (x + 2 * y < a)
            if not u: return False
    return True

for a in range(0, 100):
    if f(a):
        print(a)
        break