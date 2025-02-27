def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: return False
    return True

def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if is_prime(i): divs.add(i)
            if is_prime(n // i): divs.add(n // i)
    if divs: return sum(divs) // len(divs)
    return 0

cnt = 4

for i in range(650_001, 10**20):
    n = f(i)
    if n % 37 == 23:
        print(i, n)
        cnt -= 1
        if cnt == 0:
            break