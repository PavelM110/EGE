from fnmatch import fnmatch

def d(n):
    divs = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            if fnmatch(str(i), '*7?'): divs.add(i)
            if fnmatch(str(n // i), '*7?'): divs.add(n // i)
    divs = sorted(divs)
    return divs

for num in range(400_000, 500_001):
    divs = d(num)
    if len(divs) >= 18:
        print(num, sum(divs))