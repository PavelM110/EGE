def f(a):
    for x in range(1, 10000):
        for y in range(1, 10000):
            u = (y > 10) or (x*a > y+x)
            if not u: return False
    return True

for a in range(1, 100):
    if f(a):
        print(a)
        break