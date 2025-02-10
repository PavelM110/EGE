with open('17_4622.txt') as file:
    data = [int(i) for i in file]

maxx = min([i for i in data if i > 0 and abs(i) % 19 == 0])
ans = []

for i in range(len(data) - 1):
    n, m = data[i:i+2]
    if sum((n, m)) < maxx:
        ans.append(m + n)

print(len(ans), abs(max(ans)))