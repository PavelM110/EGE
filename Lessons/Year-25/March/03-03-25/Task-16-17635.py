from sys import setrecursionlimit

setrecursionlimit(2100)

def f(n):
    if n == 1: return 1
    return (n + 1) * f(n - 1)

print((f(2024) - 3 * f(2023)) // f(2022))