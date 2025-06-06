with open('26_12256.txt') as file:
    s, n = map(int, file.readline().split())
    data = [int(i) for i in file if i]

data = sorted(data)

boxes = [data[0]]

for i in data[1:]:
    if sum(boxes) + i <= s: boxes.append(i)

boxes = boxes[:-1]

for i in data[::-1]:
    if sum(boxes) + i <= s:
        print(len(boxes) + 1, i)
        break