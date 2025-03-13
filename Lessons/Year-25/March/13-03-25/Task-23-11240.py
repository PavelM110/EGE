def f(s, e, b):
    if s == e: return 1
    if s > e: return 0
    if b: return f(s + 2, e, 0) + f(s * 3, e, 0)
    return f(s + 2, e, 0) + f(s**2, e, 1) + f(s * 3, e, 0)

print(f(2, 64, 0))