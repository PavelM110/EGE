def f(x, y, s):
    if x + y >= 175: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, y, s - 1), f(x * 3, y, s - 1), f(x, y + 1, s - 1), f(x, y * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

def d(x, y, s):
    if x + y >= 175: return s % 2 == 0
    if s == 0: return False
    h = [d(x + 1, y, s - 1), d(x * 3, y, s - 1), d(x, y + 1, s - 1), d(x, y * 3, s - 1)]
    return any(h)

print('19)', [s for s in range(1, 155) if d(s, 19, 2)])
print('20)', [s for s in range(1, 155) if f(s, 19, 3) and not f(s, 19, 1)])
print('21)', [s for s in range(1, 155) if f(s, 19, 4) and not f(s, 19, 2)])