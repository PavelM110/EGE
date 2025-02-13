with open('17_7716.txt') as file:
    data = [int(i) for i in file if i]

def all_nech(n):
    n = str(n)
    return all(i not in n for i in '02468')

def all_ch(n):
    n = str(n)
    return all(i not in n for i in '13579')

maxx = max(i for i in data if all_nech(i))

ans = []

for i in range(len(data) - 1):
    a, b = data[i:i+2]
    summ = a + b
    ua1 = all_ch(a)
    ub1 = all_ch(b)
    u1 = ua1 or ub1
    u2 = summ > maxx
    if u1 and u2: ans.append(summ)

print(len(ans), max(ans))