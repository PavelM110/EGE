with open('26_4553.txt') as file:
    n = int(file.readline())
    data = [(int(i.split()[0]), int(i.split()[1]), i.split()[2]) for i in file if i]

m = ['0'*10001 for i in range(10002)]

for y, x, z in data:
    st = m[y]
    if z == '+':
        st = st[:x] + '1' + st[x+1:]
    else:
        st = st[:x] + '0' + st[x + 1:]
    m[y] = st

m1 = []
ans1 = 0
ans2 = 0

for i in m:
    i = i.replace('0', ' ')
    i = i.split()
    m1.append(i)

for i in range(len(m1)):
    n = m1[i]
    if n and ans1 <= len(max(n, key=len)):
        ans1 = len(max(n, key=len))
        ans2 = i

print(ans1, ans2)