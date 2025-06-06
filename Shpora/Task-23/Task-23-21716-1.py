def f(s, e):
    if s == e: return 1
    if s > e or s == 56: return 0
    return f(s + 3, e) + f(s + 7, e) + f(s * 3, e)

print(f(12, 40) * f(40, 72) * f(72, 89))