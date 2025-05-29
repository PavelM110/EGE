with open('26_3230.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data, key=lambda x: [-x[0], x[1]])

for i in range(len(data) - 1):
    r1, p1, r2, p2 = data[i][0], data[i][1], data[i+1][0], data[i+1][1]
    if r1 == r2:
        if p2 - p1 == 12:
            print(r1, p1 + 1)
            break