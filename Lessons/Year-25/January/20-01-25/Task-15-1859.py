def f(a):
    for x in range(0, 10_000):
        for y in range(0, 10_000):
            u = (2 * x + y != 70) or (x < y) or (a < x)
            if not u:
                return False
    return True

for a in range(-10_000, 10_000)[::-1]:
    if f(a): print(a); break