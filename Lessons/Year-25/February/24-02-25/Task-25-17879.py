def f(n):
    divs = []
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)
    divs = set(divs)
    if divs:
        summ = max(divs) + min(divs)
        return summ
    return 0

cnt = 0

for i in range(800_001, 10**20):
    m = f(i)
    if m % 10 == 4:
        print(i, m)
        cnt += 1
        if cnt == 5:
            break