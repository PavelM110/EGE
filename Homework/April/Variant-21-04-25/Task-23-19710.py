def f(s, e):
    if s == e: return 1
    if s > e or s == 8: return 0
    return f(s + 3, e) + f(s * 2, e)

print(f(2, 32) * f(32, 76))