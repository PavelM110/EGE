def f(s, e, t):
    if s == e: return 1
    if s > 50 or s < -50 or s in t: return 0
    return f(s + 2, e, t + [s]) + f(s - 3, e, t + [s])

print(f(1, 30, []))