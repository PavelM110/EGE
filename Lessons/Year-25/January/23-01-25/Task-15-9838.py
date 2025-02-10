def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x + 2*y > a) or (y < x) or (x < 30)):
                return False
    return True

for a in range(1, 1000)[::-1]:
    if f(a):
        print(a)
        break