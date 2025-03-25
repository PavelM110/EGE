def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            u = (x+2 <= 50) or (y < x+10) or (x>=a)
            if not u: return False
    return True

for a in range(1, 100)[::-1]:
    if f(a):
        print(a)
        break