num = 7*512**3200 + 6*256**3100 - 5*64**3000 - 4*8**2900 - 1542

cnt = 0

while num:
    if num % 64 == 0:
        cnt += 1
    num //= 64

print(cnt)