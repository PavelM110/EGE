with open('26_4604 (1).txt') as file:
    n = int(file.readline())
    data = [int(i) for i in file if i]

data = sorted(data, reverse=True)

boxes = [data[0]]

for box in data:
    if abs(box - boxes[-1]) >= 3:
        boxes.append(box)

print(len(boxes), boxes[-1])