def f(n):
    res = ''
    while n:
        res += str(n % 7)
        n //= 7
    return res[::-1]

for n in range(1, 1001)[::-1]:
    r = f(n)
    if n % 2 == 0:
        r = '52' + r + '1'
    else:
        r = r[-1] + r[1:-1] + r[0] + '15'
    r = r.lstrip('0')
    if len(r) == 4:
        print(n)
        break