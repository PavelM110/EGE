with open('17_17558.txt') as file:
    data = [int(i) for i in file if i]

del_32 = len([i for i in data if abs(i) % 32 == 0])

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    u_1 = a < 0
    u_2 = b < 0
    u1 = u_1 or u_2
    u2 = a+b < del_32
    if u1 and u2: ans.append(a+b)

print(len(ans), max(ans))