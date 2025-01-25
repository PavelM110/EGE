def s(r, b, c):
    return (r * b) > c

def f(t):
    for x in range(1, 1000):
        for y in range(1, 1000):
            u = (not s(x, y, t + 13)) <= (s(28, y, 520) or s(x, 25, 800))
            if not u:
                return False
    return True

for a in range(1, 100000)[::-1]:
    if f(a):
        print(a)
        break