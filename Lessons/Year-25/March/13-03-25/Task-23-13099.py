def f(s, e, t):
    if s == e: return 1
    if s > e + 1: return 0
    if t == 1:
        return f(s * 2, e, 0) + f(s * 3, e, 0)
    return f(s - 1, e, 1) + f(s * 2, e, 0) + f(s * 3, e, 0)

print(f(3, 15, 0))