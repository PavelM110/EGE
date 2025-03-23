alph = '0123456789ab'

def f(n):
    res  = ''
    while n:
        res += alph[n % 12]
        n //= 12
    return res[::-1]

ans = []

for n in range(1, 1000):
    r = f(n)
    if n % 3 == 0: r = '1' + r + 'b'
    else: r = '2' + r + '0'
    r = int(r, 12)
    if r < 1996:
        ans.append(r)

print(max(ans))