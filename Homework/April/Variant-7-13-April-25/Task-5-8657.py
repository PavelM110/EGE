def f(n):
    res = ''
    while n:
        res += f'{n % 3}'
        n //= 3
    return res[::-1]

for n in range(1, 1000)[::-1]:
    r = f(n)
    if n % 5 == 0:
        r += r[-3:]
    else:
        r += f((n % 5) * 5)
    r = int(r, 3)
    if r < 5496:
        print(n)
        break