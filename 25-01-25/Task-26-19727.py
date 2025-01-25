with open('26.2_19727.txt') as file:
    st = file.readline()
    data = [int(i) for i in file if i]

data = sorted(data)

m, n = map(int, st.split())

cnt_1 = 0
summ = 0

for i in data:
    if summ + i <= m:
        cnt_1 += 1
        summ += i
    else: break

cnt_2 = 0

for i in data[::-1]:
    if i + sum(data[:cnt_1 - 1]) > m:
        cnt_2 += 1
    else:
        break


print(cnt_1, cnt_2)