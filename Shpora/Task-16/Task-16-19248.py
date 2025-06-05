from sys import setrecursionlimit

setrecursionlimit(14_000)

def f(n):
    if n < 5: return n
    return 2 * n * f(n - 4)

print((f(13766) - 9 * f(13762)) // f(13758))