with open('26_4553.txt') as file:
    n = int(file.readline())
    data = [(int(i.split()[0]), int(i.split()[1]), i.split()[2]) for i in file if i]

matrix = ['0'*10001 for i in range(10002)]

for y, x, z in data:
    st = matrix[y]
    if z == '+':
        st = st[:x] + '1' + st[x+1:]
    else:
        st = st[:x] + '0' + st[x + 1:]
    matrix[y] = st

matrix1 = []
ans1 = 0
ans2 = 0

for i in matrix:
    i = i.replace('0', ' ')
    i = i.split()
    matrix1.append(i)

for i in range(len(matrix1)):
    n = matrix1[i]
    if n and ans1 <= len(max(n, key=len)):
        ans1 = len(max(n, key=len))
        ans2 = i

print(ans1, ans2)