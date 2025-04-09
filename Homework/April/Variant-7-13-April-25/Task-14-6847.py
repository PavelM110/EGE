for x in range(110, 0, -1):
    num1 = x * 111**3 + 3 * 111**2 + 2 * 111 + 1
    num2 = 211**3 + 7 * 211**2 + x * 211 + 4
    num = num1 + num2
    if num % 111 == 0:
        print(num // 111)
        break