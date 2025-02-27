def f(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: return False
    return True

cnt = 0

for i in range(600_000 - 600_000 % 6, 10**20, 6):
    if f(i+1) and f(i-1):
        print(i-1, i+1)
        cnt += 1
        if cnt == 6: break