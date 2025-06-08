with open('17_21903.txt') as file:
    data = [int(i) for i in file if i]

minn = min(i for i in data if abs(i) % 100 == 15 and 100 <= abs(i) <= 999)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    pos_a = a >= 0
    pos_b = b >= 0
    pos_c = c >= 0
    u1 = pos_a == pos_b == pos_c == pos_a
    if max(a, b, c) * min(a, b, c) > minn**2:
        if u1:
            ans.append(max(a, b, c) * min(a, b, c))

print(len(ans), min(ans))