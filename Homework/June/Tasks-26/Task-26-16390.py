with open('26_16390.txt') as file:
    s, n = map(int, file.readline().split())
    data = [int(i) for i in file if i]

data = sorted(data)

boxes = [data[0]]

for i in data[1:]:
    if sum(boxes) + i <= s: boxes.append(i)
    else: break

data = sorted(data, reverse=True)

boxes = boxes[:-1]

for i in data:
    if sum(boxes) + i <= s:
        boxes.append(i)
        break

print(len(boxes), boxes[-1])