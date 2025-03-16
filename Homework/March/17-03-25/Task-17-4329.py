with open('17_4329.txt') as file:
    data = [int(i) for i in file if i]

def l(a):
    return len(d(a))

def d(n):
    divs = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    divs = sorted(divs)
    return set(divs)

max_d = d(max(data, key=l))

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    da = d(a)
    db = d(b)
    if len(da & max_d) >= 3 and len(db & max_d) >= 3:
        ans.append(len(da & db))

print(len(ans), max(ans))
