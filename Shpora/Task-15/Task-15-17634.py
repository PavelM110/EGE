def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            u = (x+y <= 30) or (y <= x+2) or (y >= a)
            if not u: return False
    return True

for a in range(0, 1000)[::-1]:
    if f(a):
        print(a)
        break