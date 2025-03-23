def f(s, e):
    if s == e: return 1
    if s > e: return 0
    return f(s + 1, e) + f(s + 2, e) + f(s * 2, e)

print(f(4, 11) * f(11, 13) * f(13, 15))