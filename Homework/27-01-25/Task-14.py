for x in range(1, 150)[::-1]:
    num1 = 5*150**3 + 1*150**3 + x*150**2 + 2*150 + 9
    num2 = x*150**3 + 0*150**2 + 2*150 + 3
    num = num1 + num2
    if num % 4 == 0:
        print(num //4)
        break