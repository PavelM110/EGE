def f(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: return False
    return True

cnt = 0

for i in range(194441, 196501):
    if f(i):
        if i % 100 == 93:
            cnt += 1
            print(cnt, i)