def f(s, e):
    if s == e: return 1
    if int(s) > int(e): return 0
    return f(bin(int(s, 2) + 1)[2:], e) + f(s + '1', e) + f(s + '0', e)

print(f('100', '11101'))