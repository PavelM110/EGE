from fnmatch import fnmatch

def d(n):
    divs = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            if i % 2 == 0: divs.add(i)
            if (n // i) % 2 == 0: divs.add(n // i)
    divs = sorted(divs)
    return divs

ans = []

for num in range(65001, 10**20):
    if fnmatch(str(num), '6*97*5?'):
        divs = d(num)
        if len(divs) >= 4:
            ans.append((num, sum(divs)))
            if len(ans) == 7: break

for i in sorted(ans):
    print(*i)