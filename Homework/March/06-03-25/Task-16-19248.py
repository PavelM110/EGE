from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 5: return n
    return 2 * n * f(n - 4)

for i in range(13766):
    f(i)

print((f(13766) - 9*f(13762)) // f(13758))