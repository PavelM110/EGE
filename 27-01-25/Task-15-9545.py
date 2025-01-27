def d(x, d):
    return x % d == 0

def f(a):
    for x in range(1, 1000):
        u = (d(x, 10) and d(x, 26) and (x >= 300)) <= (a <= x)
        if not u:
            return False
    return True

for a in range(1, 1000)[::-1]:
    if f(a):
        print(a)
        break