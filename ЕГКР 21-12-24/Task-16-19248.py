from sys import setrecursionlimit

setrecursionlimit(4_000)

def f(num):
    return num if num < 5 else 2*num*f(num-4)

print((f(13766) - 9*f(13762))//f(13758))