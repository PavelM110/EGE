def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if is_prime(i): divs.add(i)
            if is_prime(n // i): divs.add(n // i)
    if len(divs):
        return sum(divs)
    return 0

cnt = 7

for i in range(32_500_001, 10**20):
    s = f(i)
    if s and s % 145 == 0:
        print(i, s)
        cnt -= 1
        if not cnt:
            break