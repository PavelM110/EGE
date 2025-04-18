from functools import lru_cache

@lru_cache(None)
def f(n):
    if n > 400: return n ** n
    return n + 6 + f(n + 12)

for n in range(401, 0, -1):
    f(n)

print(f(72) - f(108))