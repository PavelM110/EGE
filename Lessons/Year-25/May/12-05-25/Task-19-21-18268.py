from math import ceil

def f(x, y, s):
    if x + y <= 72: return s % 2 == 0
    if s == 0: return False
    h = [f(x - 3, y, s - 1),
         f(x, y - 3, s - 1),
         f(ceil(x / 2), y, s - 1),
         f(x, ceil(y / 2), s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(23, 1000) if f(50, s, 2)]) # 94
print('19)', [s for s in range(23, 1000) if f(50, s, 3) and not f(50, s, 1)])
print('19)', [s for s in range(23, 1000) if f(50, s, 4) and not f(50, s, 2)])