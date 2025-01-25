def f(a):
    for x in range(90, 101):
        f = not(x & 79 == 0) and ((x & 31 == 0) <= (not(x & a == 0)))
        if not f:
            return False
    return True

for a in range(0, 100):
    if f(a):
        print(a)
        break