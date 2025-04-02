def f(s, e, t):
    if s == e: return 1
    if s > e + 1: return 0
    if t:
        return f(s - 1, e, 0) + f(s*2, e, 1) + f(s*3, e, 1)
    return f(s*2, e, 1) + f(s*3, e, 1)

print(f(3, 15, 1))