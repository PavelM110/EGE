with open('17_18617.txt') as file:
    data = [int(i) for i in file if i]

max_3 = max(data) % 3
min_7 = min(data) % 7

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i + 2]
    u1 = a % 3 == max_3 or b % 3 == max_3
    u2 = a % 7 == min_7 or b % 7 == min_7
    if u1 and u2:
        ans.append(a + b)

print(len(ans), max(ans))