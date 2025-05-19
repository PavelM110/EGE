with open('24_2421.txt') as file:
    data =file.readline()

data = data.replace('D', ' ').split()

print(len(max(data, key=len)))