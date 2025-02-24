def f(n):
    for i in range(18, n // 2 + 1, 10):
        if n % i == 0: return i
    return 0

cnt = 0

for i in range(500000, 10**9):
    if cnt == 5: break
    n = f(i)
    if n:
        print(i, n)
        cnt += 1