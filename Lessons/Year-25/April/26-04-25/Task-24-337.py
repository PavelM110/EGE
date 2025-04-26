with open('24-337.txt') as file:
    data = file.readline()

from string import ascii_uppercase

for i in ascii_uppercase[4:]:
    data = data.replace(i, ' ')

data = data.split()

anses = []

for st in data:
    ans = 0
    for i in range(len(st)):
        if st[i] == '1':
            for j in range(i,len(st) + 1)[::-1]:
                if st[i:j] and int(st[i:j], 14) % 7 == 0:
                    ans = max(ans, len(st[i:j]))
    anses.append(ans)

print(max(anses))

