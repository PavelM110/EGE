def f(s, e):
    if s == e: return 1
    if s > e or s == 9: return 0
    return f(s + 1, e) + f(s * 2, e)

print(f(2, 12) * f(12, 42))