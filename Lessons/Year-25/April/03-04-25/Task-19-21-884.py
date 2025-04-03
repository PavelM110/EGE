def f(x, y, s):
    if x + y >= 30: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, y, s - 1),
         f(x * 2, y, s - 1),
         f(x, y + 1, s - 1),
         f(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

cnt_19 = 0

for s in range(1, 30):
    for k in range(1, 30):
        if s+k < 30:
            if f(s, k, 2):
                cnt_19 += 1

print('19)', cnt_19)

print('20)', [s for s in range(1, 30) if f(6, s, 3) and not f(6, s, 1)])

cnt_21 = 0

for s in range(1, 30):
    for k in range(1, 30):
        if s+k < 30:
            if f(s, k, 4) and not f(s, k, 2):
                cnt_21 += 1

print('21)', cnt_21)