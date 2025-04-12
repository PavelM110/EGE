from re import finditer

with open('24_9845.txt') as file:
    data = file.readline()

pat = r'((((?<=[89])[ABC][89])|((?<=[ABC])[89][ABC])))+'

matches = finditer(pat, data)

matches = [i.group() for i in matches]

print(len(max(matches, key=len)))