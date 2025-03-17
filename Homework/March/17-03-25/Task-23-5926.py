from functools import lru_cache

@lru_cache(None)
def f(s, p, l):
    if p == 24: return [s]
    if l == 1:
        return f(s + 7, p + 1, 2) + f(s * 4, p + 1, 3)
    if l == 2:
        return f(s + 1, p + 1, 1) + f(s * 4, p + 1, 3)
    if l == 3:
        return f(s + 1, p + 1, 1) + f(s + 7, p + 1, 2)
    return f(s + 1, p + 1, 1) + f(s * 4, p + 1, 3) + f(s + 7, p + 1, 2)

print(len(set(f(1, 0, 0))))