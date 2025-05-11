with open('17_6089.txt') as file:
    data = [int(i) for i in file if i]

max_2 = max(i for i in data if abs(i) % 10 == 2)

ans = []

for i in data:
    j = abs(i)
    if j % 3 == 0:
        if j % 7 and j % 17:
            if abs(max_2) % j == 0:
                ans.append(i)

print(len(ans), max(ans))