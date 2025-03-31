def f(x, y, s):
    if x + y >= 65: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x + 1, y, s - 1),
        f(x * 3, y, s - 1),
        f(x, y + 1, s - 1),
        f(x, y * 3, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

def d(x, y, s):
    if x + y >= 65: return s % 2 == 0
    if s == 0: return False
    h = [
        d(x + 1, y, s - 1),
        d(x * 3, y, s - 1),
        d(x, y + 1, s - 1),
        d(x, y * 3, s - 1)
    ]
    return any(h)

print('19)', [s for s in range(1, 59) if d(s, 6, 2)])
print('20)', [s for s in range(1, 59) if f(s, 6, 3) and not f(s, 6, 1)])
print('21)', [s for s in range(1, 59) if f(s, 6, 4) and not f(s, 6, 2)])