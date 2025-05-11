ans = set()

for n in range(100, 1001):
    r = bin(n)[2:]
    r = r.replace('0', '')
    r = int(r, 2)
    ans.add(r)

print(len(set(ans)))