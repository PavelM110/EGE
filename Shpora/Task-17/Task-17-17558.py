with open('17_17558.txt') as file:
    data = [int(i) for i in file if i]

c_32 = len([i for i in data if abs(i) % 32 == 0])

ans = []

for i in range(len(data) - 1):
        a, b = data[i:i+2]
        ua1 = a < 0
        ub1 = b < 0
        u1 = ua1 or ub1
        if u1 and a + b < c_32:
            ans.append(a + b)

print(len(ans), max(ans))