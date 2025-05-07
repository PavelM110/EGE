def f(n):
    divs = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            if str(i)[0] == '4':
                divs.add(i)
            if str(n // i)[0] == '4':
                divs.add(n // i)
    if len(divs) == 24:
        return max(divs)
    return 0

for i in range(10**6):
    d = f(i)
    if d:
        print(i, d)