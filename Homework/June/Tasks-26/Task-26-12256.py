with open('26_12256.txt') as file:
    s, n = map(int, file.readline().split())
    data = [int(i) for i in file if i]

data = sorted(data)

boxes = [data[0]]

for i in data[1:]:
    if sum(boxes) + i <= s: boxes.append(i)
    else: break

boxes = boxes[:-1]

data = sorted(data, reverse=True)

for i in data:
    if i + sum(boxes) <= s:
        boxes.append(i)
        break

print(len(boxes), boxes[-1])