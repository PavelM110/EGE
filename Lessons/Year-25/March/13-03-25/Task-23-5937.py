def f(s, e, c):
    if s == e:
        return c <= 15
    if s > e: return 0
    if s % 2 == 0:
        return f(s + 2, e, c + 1) + f(s + 3, e, c + 1) + f(s * 2 + 1, e, c + 1)
    return f(s + 2, e, c) + f(s + 3, e, c) + f(s * 2 + 1, e, c)

print(f(1, 55, 0))