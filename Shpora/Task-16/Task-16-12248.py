from sys import setrecursionlimit

setrecursionlimit(3000)

def f(n):
    if n<= 3: return 1
    return (n + 3) * f(n - 2)

print(f(2028) // f(2024))