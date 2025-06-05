def f(s, e):
    if s == e: return 1
    if s < e or s in (9, 16): return 0
    return f(s - 1, e) + f(s - 2, e) + f(s // 3, e)

print(f(19, 3))