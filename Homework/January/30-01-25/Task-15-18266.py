def f(a):
    for x in range(1, 1000):
        u = (x&57 == 0) or ((x&23 == 0) <= (not(x&a == 0)))
        if not u: return False
    return True

for a in range(1, 100):
    if f(a):
        print(a)
        break