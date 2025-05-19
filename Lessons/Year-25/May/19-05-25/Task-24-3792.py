with open('24_3792.txt') as file:
    data = file.readline()

data = data.replace('D', ' ').replace('E', ' ').split()

print(len(max(data, key=len)))