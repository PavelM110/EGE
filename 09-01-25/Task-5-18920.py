res = []

for n in range(1, 26):
    r = bin(n)[2:]
    if n % 2:
        r = '10' + r + '1'
    else:
        r = '10' + r + '0111'
    r = int(r, 2)
    res.append(r)

print(max(res))