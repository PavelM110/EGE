def f(a):
    for x in range(1, 10_000):
        for y in range(1, 10_000):
            if not((y >= a) or (x + y <= 22) or (y <= (x - 6))): return False
    return True

for a in range(1, 50)[::-1]:
    if f(a):
        print(a)
        break