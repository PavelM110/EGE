def f(n, e):
    if n in (36, 100): return 0
    if n == e: return 1
    if n < e: return 0
    if n > e: return f(n//3, e) + f(n//2, e) + f(n-3, e)

print(f(163, 45) * f(45, 3))