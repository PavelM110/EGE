def f(x, y, s):
    if x + y >= 127: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 2, y, s - 1), f(x * 3, y, s - 1), f(x, y + 2, s - 1), f(x, y * 3, s - 1)]
    return any(h)

print('19)', [s for s in range(1, 123) if f(2, s, 2)])

def g(x, y, s):
    if x + y >= 127: return s % 2 == 0
    if s == 0: return False
    h = [g(x + 2, y, s - 1), g(x * 3, y, s - 1), g(x, y + 2, s - 1), g(x, y * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('20)', [s for s in range(1, 123) if g(s, 2, 3) and not g(s, 2, 1)])
print('21)', [s for s in range(1, 123) if g(s, 2, 4) and not g(s, 2, 2)])