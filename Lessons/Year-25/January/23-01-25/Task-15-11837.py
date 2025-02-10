def f(a):
    for x in range(1, 2000):
        for y in range(1, 2000):
            if not((x**2 + y**2 > 1024 - x) or (y < -2*x +a)):
                return False
    return True

for a in range(1, 100):
    if f(a):
        print(a)
        break