def f(x, s, l):
    if x > 40: return s % 2 == 0
    if s == 0: return False
    if l == 1:
        h = [
            f(x + 6, s - 1, 2),
            f(x * 2, s - 1, 3)
        ]
    elif l == 2:
        h = [
            f(x + 3, s - 1, 1),
            f(x * 2, s - 1, 3)
        ]
    elif l == 3:
        h = [
            f(x + 3, s - 1, 1),
            f(x + 6, s - 1, 2)
        ]
    else:
        h = [
            f(x + 3, s - 1, 1),
            f(x + 6, s - 1, 2),
            f(x * 2, s - 1, 3)
        ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(2, 37) if f(s, 2, 0)])
print('20)', [s for s in range(2, 37) if f(s, 3, 0) and not f(s, 1, 0)])
print('21)', [s for s in range(2, 37) if f(s, 4, 0) and not f(s, 2, 0)])