from re import finditer

with open('24_4627.txt') as file:
    data = file.readline()

pat = r'(PNO|NPO)+'

matches = finditer(pat, data)

matches = [i.group() for i in matches]

print(len(max(matches, key=len)) // 3)