def p(n):
    if n < 2: return False
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: return False
    return True

def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if p(i): divs |= {i}
            if p(n // i): divs |= {n // i}
    divs = sorted(divs)
    if len(divs): return sum(divs)
    return 0

cnt = 7

for i in range(32_500_001, 10**10):
    s = f(i)
    if s and s % 145 == 0:
        print(i, s)
        cnt -= 1
        if not cnt: break