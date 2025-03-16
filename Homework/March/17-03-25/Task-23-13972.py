def f(s, e, p):
    if s == e: return 1
    if s > e: return 0
    if p:
        return f(s + 2, e, 0) + f(s * 2, e, 0)
    return f(s + 2, e, 0) + f(s * 2, e, 0) + f(s + 5, e, 0)

print(f(7, 23, 1) * f(23, 35, 0))