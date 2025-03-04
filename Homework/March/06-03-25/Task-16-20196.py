from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 110: return n
    return n + f(n - 1)

for i in range(2026):
    f(i)

print(f(2025) - f(2021))