def f(s, e, c):
    if s == e: return c
    if s > e: return 0
    if s ** .5 % 1 == 0: return f(s - 1, e, c + 1)
    return max(f(s + 2, e, c), f(s + 3, e, c), f(s * 3, e, c))

print(f(5, 50, 0))

def g(s, e, c):
    if s == e: return c == 2
    if s > e: return 0
    if s ** .5 % 1 == 0: return g(s - 1, e, c + 1)
    return g(s + 2, e, c) + g(s + 3, e, c) + g(s * 3, e, c)

print(g(5, 50, 0))
