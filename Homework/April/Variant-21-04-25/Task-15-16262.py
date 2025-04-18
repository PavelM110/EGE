def f(a):
    for x in range(-100, 100):
        for y in range(-100, 100):
            u = ((a < x) or ((x**2 - 7*x + 10) > 0)) and ((a >= y) or ((y**2 + 7*y + 12) > 0))
            if not u:
                return False
    return True

cnt = 0

for a in range(-100, 100):
    if f(a): cnt += 1

print(cnt)