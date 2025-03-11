from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 11: return n
    if n % 2:
        return 3 * n - 4 + f(n - 3)
    return 2 * n - 3 + f(n - 2)

for i in range(5501):
    f(i)

print(f(5500) - f(5497))