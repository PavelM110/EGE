def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: return False
    return True

def f(n):
    divs = set()
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if is_prime(i): divs.add(i)
            if is_prime(n // i): divs.add(n // i)
    divs = sorted(divs)
    if divs: return min(divs) + max(divs)
    return 0

cnt = 0

for i in range(1_200_000, 10**20):
    m = f(i)
    if m:
        if m > 2000 and m % 10 == 8:
            print(i, m)
            cnt += 1
            if cnt == 5: break