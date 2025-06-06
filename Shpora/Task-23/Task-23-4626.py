def f(s, e):
    if s == e: return 1
    if s < e: return 0
    return f(s - 2, e) + f(s // 2, e)

print(f(28, 10) * f(10, 1))