def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

for n in range(1, 1000):
    r = f(n)
    if sum(map(int, r)) % 2 == 0: r = '12' + r[2:] + '0'
    else: r = '10' + r[2:] + '2'
    r = int(r, 3)
    if r > 105:
        print(n)
        break