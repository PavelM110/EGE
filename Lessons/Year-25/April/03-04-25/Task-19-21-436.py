def f(x, y , s):
    if x + y >= 44: return s % 2 == 0
    if s == 0: return False
    h = [f(x + y, y, s - 1),
         f(x, y + x, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 100) if f(11, s, 1)])
print('20)', [s for s in range(1, 100) if f(11, s, 2)])

ans = []

for x in range(1, 30):
    for y in range(1, 30):
        if f(x, y, 3):
            ans.append((abs(x - y), x, y))

print('21)',min(ans))