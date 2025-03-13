def f(s, e, c1, c2, c3):
    if s == e:
        return c1 <= 4 and c2 >= 2 and c3 == 5
    if s > e: return 0
    return f(s * 5, e, c1 + 1, c2, c3) + f(s * 3, e, c1, c2 + 1, c3) + f(s + 45, e, c1, c2, c3 + 1)

print(f(1, 2970, 0, 0, 0))