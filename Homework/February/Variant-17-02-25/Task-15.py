def f(a):
    for x in range(90, 101):
        u = (not(x&79 == 0)) and ((x&31 == 0) <= (not(x&a == 0)))
        if not u: return False
    return True

for a in range(0, 100):
    if f(a):
        print(a)
        break