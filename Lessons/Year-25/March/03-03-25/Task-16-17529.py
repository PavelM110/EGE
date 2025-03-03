from sys import setrecursionlimit

setrecursionlimit(2100)

def f(n):
    if n == 1: return 1
    return n * f(n - 1)

print((2 * f(2024) + f(2023)) // f(2022))