def f(a):
    for x in range(100000):
        u = ((x & 84653 != 0) or (x & 51763 != 0)) <= ((x & a) > 0)
        if not u: return False
    return True

for a in range(1, 1000000):
    if f(a):
        print(a)
        break