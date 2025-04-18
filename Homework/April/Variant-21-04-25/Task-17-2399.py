with open('17_2399.txt') as file:
    data = [int(i) for i in file if i]

del_35 = sum(sum(map(int, str(i))) for i in data if i % 35 == 0)

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    ua1 = a > del_35
    ub1 = b > del_35
    if ua1 and ub1:
        u2 = False
    elif ua1 and not ub1:
        u2 = hex(b)[-2:] == 'ef'
    elif ub1 and not ua1:
        u2 = hex(a)[-2:] == 'ef'
    else:
        u2 = False
    if u2:
        ans.append(a + b)

print(len(ans), min(ans))