from re import *

with open('24_11636.txt') as file:
    data = file.readline()

# data = 'AA@@@AA@A@A@AA'


cnt = 0

# for i in range(len(data)):
#     if data[i] == 'A':
#         for j in range(i + 2, len(data)):
#             if data[j] == 'A':
#                 cnt += 1
#
# print(cnt)

# for i in range(len(data)):
#     if data[i] == 'A':
#         cnt += len(list(finditer('A', data[i + 2:])))
#
# print(cnt)

indexes = [i for i in range(len(data)) if data[i] == 'A']

cnt = 0

for i in range(len(indexes) - 1):
    cnt_in = 0
    cnt_in += len(indexes[1+i:])
    if indexes[i+1] - indexes[i] == 1:
        cnt_in -= 1
    cnt += cnt_in

print(cnt)