def f(x, s):
    if 36 <= x <= 85: return s % 2 == 0
    if x > 85: return (s + 1) % 2 == 0
    if s == 0: return False
    h = [f(x + 2, s - 1),
         f(x * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('_'*15+'19'+'_'*15)

for p in range(1, 10):
    if f(30, p):
        if p % 2: print(30, 'P')
        else: print(30, 'B')
    if f(32, p):
        if p % 2: print(32, 'P')
        else: print(32, 'B')

print('_'*15+'20'+'_'*15)

for p in range(1, 10):
    if f(8, p):
        if p % 2: print(8, 'P')
        else: print(8, 'B')
    if f(10, p):
        if p % 2: print(10, 'P')
        else: print(10, 'B')

print('_'*15+'21'+'_'*15)

for p in range(1, 10):
    if f(6, p):
        if p % 2: print(8, 'P')
        else: print(8, 'B')
        break
