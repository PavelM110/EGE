def d(x, y): return x % y == 0

def f(a):
    for x in range(1, 1000):
        u = ((not d(x, 7)) and d(x, 13)) <= (x > a - 40)
        if not u: return False
    return True

for a in range(1, 100)[::-1]:
    if f(a):
        print(a)
        break