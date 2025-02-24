def f(n):
    divs = []
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)
    divs = sorted(set(divs))
    for i in divs:
        if i != 8 and i % 10 == 8: return i

cnt = 0

for i in range(500001, 10**9):
    n = f(i)
    if n:
        print(i, n)
        cnt += 1
        if cnt == 5: break
