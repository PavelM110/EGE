with open('24_11636.txt') as file:
    data = file.readline()

indexes = [i for i in range(len(data)) if data[i] == 'A']

cnt = 0

for i in range(len(indexes) - 1):
    cnt_in = 0
    cnt_in += len(indexes[1+i:])
    if indexes[i+1] - indexes[i] == 1:
        cnt_in -= 1
    cnt += cnt_in

print(cnt)