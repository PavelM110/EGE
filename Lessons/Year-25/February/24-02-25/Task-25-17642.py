def f(n):
    divs = []
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs.append(n // i)
            divs.append(i)
    divs = sorted(set(divs))
    for i in divs:
        if i != 9 and i % 10 == 9:
            return i
    return 0

cnt = 0

for i in range(800_001, 10**20):
    n = f(i)
    if n:
        print(i, n)
        cnt += 1
        if cnt == 5:
            break