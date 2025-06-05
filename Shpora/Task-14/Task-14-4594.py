num = 4 * 625**1920 + 4 * 125**1930 - 4 * 25**1940 - 3 * 5**1950 - 1960

cnt = 0

while num:
    cnt += num % 5 == 0
    num //= 5

print(cnt)