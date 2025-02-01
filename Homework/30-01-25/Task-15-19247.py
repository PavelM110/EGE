def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            u = (x - 3*y < a) or (y > 400) or (x > 56)
            if not u: return False
    return True

for a in range(0, 100):
    if f(a):
        print(a)
        break