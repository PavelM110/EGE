def pal(num):
    return str(num) == str(num)[::-1]

def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs)
    if len(divs):
        return max(divs)
    return 0

cnt = 5

for i in range(10**9 + 1, 10**20):
    if pal(i):
        n = f(i)
        if n:
            print(i, n)
            cnt -= 1
            if not cnt:
                break