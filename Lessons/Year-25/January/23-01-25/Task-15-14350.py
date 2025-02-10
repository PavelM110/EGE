def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x < 7) or (y >= 3*x + a - 20) or (x >= 34) or (y < 121)
            if not(f):
                return False
    return True

for a in range(1, 1000)[::-1]:
    if f(a):
        print(a)
        break