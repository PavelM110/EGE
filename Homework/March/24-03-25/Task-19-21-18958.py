def f(s, p):
    if s >= 666: return p % 2 == 0
    if p == 0: return False
    h = [f(s+3, p - 1), f(s*3, p - 1), f(s + s**2, p - 1)]
    return any(h) if (p - 1) % 2 == 0 else all(h)

print('20)', [s for s in range(0, 666) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(666) if f(s, 4) and not f(s, 2)])