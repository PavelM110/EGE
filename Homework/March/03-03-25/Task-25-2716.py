def f(n):
    divs = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if i <= n / 2: divs.add(i)
            if n // i <= n / 2: divs.add(n // i)
    divs = sorted(divs, reverse=True)
    if len(divs) >= 3:
        return divs[:3]
    return (0, 0, 0)

ans = []

for n in range(1_200_001)[::-1]:
    s = sum(f(n))
    if s and s % 2022 == 0 and s != n:
        ans.append((n, s))
        if len(ans) == 5: break

for i in sorted(ans):
    print(*i)