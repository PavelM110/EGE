def f(s, e):
    if s == e: return 1
    if s > e or s == 17: return 0
    return f(s + 2, e) + f(s + 3, e) + f(s * 2, e)

print(f(3, 10) * f(10, 25))