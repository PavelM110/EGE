def f(s, e, l):
    if s == e: return l != 'c'
    if s > e: return 0
    return f(s + 2, e, 'a') + f(s + 5, e, 'b') + f(s ** 2, e, 'c')

print(f(4, 36, '1'))