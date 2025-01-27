from sys import setrecursionlimit

setrecursionlimit(5000)

def f(n):
    if n > 3000: return n
    if n <= 3000 and n % 2 == 0: return n + f(n + 1) + 1
    if n <= 3000 and n % 2 == 1: return f(n + 2) + 2

print(f(40) - f(43))