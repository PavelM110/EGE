def f(b):
    for x in range(0, 1000):
        u = (((x & 500) != 0) and ((x & 200) == 0)) <= (not((x & b) == 0))
        if not u: return False
    return True

for b in range(1, 1000):
    if f(b):
        print(b)
        break