from re import *

with open('24-333.txt') as file:
    data = file.readline()

# data = 'alex@@s..ch@gmail.com.runet@yandex.rubo@yandex.ru'
name = r'([\.a-zA-Z0-9]([0-9a-zA-Z]+\.)+[a-zA-Z0-9]+)'
server = r'(@yandex.ru|@gmail.com)'
address = rf'{name}{server}'

matches = finditer(address, data)

# print(*matches)

ans = 0

for i in matches:
    i = i.group()
    ans = max(ans, len(i))

print(ans)