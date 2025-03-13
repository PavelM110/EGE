def f(s, e, t):
    if s == e:
        return len(set(t.split())) == 51
    if s > e: return 0
    return f(s * 4, e, t + str(s) + ' ') + f(s + 1, e, t + str(s) + ' ') + f(s * 3, e, t + str(s) + ' ')

print(f(2, 404,''))