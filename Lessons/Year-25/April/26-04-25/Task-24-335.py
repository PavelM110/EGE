from re import *

with open('24-335.txt') as file:
    data = file.readline()

num_a = r'([1-9]\d*[^05()+-])'
num_b = r'([1-9]\d*[05])'
# minus = rf'\({num_a}-{num_b}\)'
# plus = rf'\({num_a}\+{num_b}\)'
pat = rf'(\({num_a}[+-]{num_b}\))+'

matches = finditer(pat, data)

ans = 0

for i in matches:
    i = i.group()
    # i = i.split(')(')
    ans = max(ans, len(i))

print(ans)