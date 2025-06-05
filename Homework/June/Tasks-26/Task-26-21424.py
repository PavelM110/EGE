with open('26_21424.txt') as file:
    n = int(file.readline())
    data = [int(i) for i in file if i]

data = sorted(data, reverse=True)

boxes = [data[0]]

for i in data:
    if boxes[-1] - i >= 9:
        boxes.append(i)

print(len(boxes), boxes[-1])