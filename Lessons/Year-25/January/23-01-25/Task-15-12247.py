def f(a):
    for x in range(1, 1000):
        f = (x & a == 0) or not(x & 37 == 0) or not(x & 12 == 0)
        if not f:
            return False
    return True

for a in range(1, 1000)[::-1]:
    if f(a):
        print(a)
        break