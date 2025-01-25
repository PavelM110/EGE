def g(n):
    maxx = int(max(str(n)))
    return n + maxx

def f(s, e):
    if s == e: return 1
    if s > e: return 0
    if s < e: return f(s + 2, e) + f(g(s), e)

print(f(32, 55) + f(55, 76))