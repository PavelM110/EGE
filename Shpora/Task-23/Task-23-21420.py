def f(s, e):
    if s == e: return 1
    if s > e or s == 35: return 0
    return f(s + 1, e) + f(s + 2, e) + f(s * 2, e)

print(f(7, 13) * f(13, 15) * f(15, 51))