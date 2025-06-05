def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            u = ((2*x + y) != 70) or (x < y) or (a < x)
            if not u: return False
    return True

for a in range(-100, 1000)[::-1]:
    if f(a):
        print(a)
        break