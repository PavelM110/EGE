with open('17_19486.txt') as file:
    data = [int(i) for i in file if i]

cnt_7 = sum(1 for i in data if abs(i) % 10 == 7)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i + 2]
    summ = a + b
    u1 = (a * b)< 0
    u2 = summ < cnt_7
    if u1 and u2: ans.append(summ)

print(len(ans), max(ans))