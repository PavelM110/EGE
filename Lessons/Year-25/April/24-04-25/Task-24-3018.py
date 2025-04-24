from re import *

with open('24_3018.txt') as file:
    data = file.readline()

pat = r'(?<=A)[^AB]{15,}(?=A)'

matches = finditer(pat, data)

print(len(list(matches)))