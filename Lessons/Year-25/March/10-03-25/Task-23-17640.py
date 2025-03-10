def f(s, e):
    if s == e: return 1
    if s < e: return 0
    return f(s - 2, e) + f(s // 2, e)

print(f(32, 14) * f(14, 1))