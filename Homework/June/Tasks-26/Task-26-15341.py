with open('26_15341.txt') as file:
    n = int(file.readline())
    data = [int(i) for i in file if i]

data = sorted(data, reverse=True)

layers = [data[0]]

for i in data:
    if layers[-1] - i >= 8: layers.append(i)

print(len(layers), layers[-1])