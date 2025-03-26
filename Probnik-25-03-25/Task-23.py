def f(s, e):
    if s == e: return 1
    if s > e or s == 8: return 0
    return f(s + 1, e) + f(s * 2, e) + f(s * 5, e)

print(f(2, 27) * f(27, 54))