def f(x, y, p):
    if x * y >= 777 and p == 3: return True
    if x * y >= 777 and p != 3: return False
    if x * y < 777: return (f(x * 2, y, p+1) or f(x + 3, y, p+1) or f(x, y*2, p+1) or f(x, y+3, p+1))

for s in range(1, 111):
    if f(7, s, 1):
        print(s)
        break