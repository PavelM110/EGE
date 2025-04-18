for n in range(1, 1000):
    r = bin(n)[2:]
    r = r.replace('0', '@').replace('1', '0').replace('@', '1')
    r = '1' + r
    r += str(r.count('1') % 2)
    r = int(r, 2)
    if r > 180:
        print(n)
        break