from re import *

with open('24_19149.txt') as file:
    data = file.readline()

pattern = r'\(\d+(\+\d+)*+\)'

matches = finditer(pattern, data)

ans = ''

for match in matches:
    match = match.group()
    print(match)
    if len(ans) < len(match):
        if eval(match) % 2 == 0:
            ans = match

print(ans, len(ans))