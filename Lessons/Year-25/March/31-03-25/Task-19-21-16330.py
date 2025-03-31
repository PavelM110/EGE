def f(x, y, s):
    if x + y >= 59: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, y, s - 1), f(x * 2, y, s - 1), f(x, y + 1, s - 1), f(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

def d(x, y, s):
    if x + y >= 59: return s % 2 == 0
    if s == 0: return False
    h = [d(x + 1, y, s - 1), d(x * 2, y, s - 1), d(x, y + 1, s - 1), d(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else any(h)

print('19)', [s for s in range(1, 54) if d(s, 5, 2)])
print('20)', [s for s in range(1, 54) if f(s, 5, 3) and not f(s, 5, 1)])
print('21)', [s for s in range(1, 54) if f(s, 5, 4) and not f(s, 5, 2)])

