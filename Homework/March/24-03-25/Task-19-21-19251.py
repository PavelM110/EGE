def f(s, p):
    if s >= 132: return p % 2 == 0
    if p == 0: return False
    h = [f(s + 3, p - 1), f(s + 6, p - 1), f(s * 3, p - 1)]
    return any(h) if (p - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 132) if f(s, 2)])
print('20)', [s for s in range(1, 132) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(1, 132) if f(s, 4) and not f(s, 2)])