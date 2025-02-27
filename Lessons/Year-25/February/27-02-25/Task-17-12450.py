with open('17_12450.txt') as file:
    data = [int(i) for i in file if i]

min_52 = min(i for i in data if i % 52 == 0)

ans = []

for i in range(len(data) - 2):
    a, b, c = data[i:i + 3]
    summ_o = sum(i % 113 for i in (a, b, c))
    u1 = summ_o == min_52
    if u1:
        ans.append(a+b+c)

print(len(ans), max(ans))