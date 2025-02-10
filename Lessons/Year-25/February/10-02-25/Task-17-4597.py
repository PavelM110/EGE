with open('17_4597.txt') as file:
    data = [int(i) for i in file if i]

minn = min(data)
cnt = 0
ans = []

for i in range(len(data) - 1):
    n, m = data[i:i+2]
    if n % 117 == minn or m % 117 == minn:
        cnt += 1
        ans.append(sum((n, m)))

print(cnt, max(ans))