def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    if len(divs):
        return sum(divs) // len(divs)
    return 0

cnt = 7

for i in range(1, 700_000)[::-1]:
    m = f(i)
    if str(m)[-3:] == '313':
        print(i, m)
        cnt -= 1
        if not cnt:
            break